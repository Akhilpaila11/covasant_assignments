from flask import Flask, request, redirect, url_for
app = Flask(__name__)
notepad_content = ""

@app.route("/updatefortoday", methods=['GET', 'POST'])
def update_for_today():
    global notepad_content
    if request.method == 'POST':
        notepad_content = request.form.get('note', '')
        return "Note updated successfully!"
    return '''
        <form method="post">
            <textarea name="note" rows="10" cols="40">{}</textarea><br>
            <input type="submit" value="Update">
        </form>
    '''.format(notepad_content)

@app.route("/share", methods=['GET'])
def share():
    return f"<h2>Shared Note:</h2><pre>{notepad_content}</pre>"

@app.route("/clearnotepadtxt", methods=['GET'])
def clear_notepad_txt():
    global notepad_content
    notepad_content = ""
    return "Notepad content cleared."

if __name__ == "__main__":
    app.run(debug=True)
