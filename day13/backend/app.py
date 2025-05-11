from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory 
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
llm = ChatMistralAI(model="mistral-small", temperature=0.7, api_key=api_key)

app = Flask(__name__, static_folder="build", static_url_path="/")
CORS(app)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Mistral, a helpful AI assistant. Respond clearly and concisely."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
chain: Runnable = prompt | llm

message_histories = {}
conversation_log = []

def get_memory(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in message_histories:
        message_histories[session_id] = InMemoryChatMessageHistory()
    return message_histories[session_id]

conversation = RunnableWithMessageHistory(
    chain,
    get_memory,
    input_messages_key="input",
    history_messages_key="history"
)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('query')
    session_id = data.get('session_id', 'default')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    result = conversation.invoke(
        {"input": user_query},
        config={"configurable": {"session_id": session_id}}
    )

    conversation_log.append({"sender": "user", "text": user_query})
    conversation_log.append({"sender": "mistral", "text": result.content})

    return jsonify({"result": result.content})

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify({"history": conversation_log})

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    message_histories.clear()
    conversation_log.clear()
    return jsonify({"message": "History cleared"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
