import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState(''); 
  const [history, setHistory] = useState([]); 
  const [fullHistory, setFullHistory] = useState([]); 
  const [showFullHistory, setShowFullHistory] = useState(false); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setHistory(prev => [...prev, { sender: 'user', text: query }]);

    try {
      const response = await axios.post('/api/chat', { query }); 
      const botResponse = response.data.result; 

      setHistory(prev => [...prev, { sender: 'bot', text: botResponse }]);
    } catch (error) {
      console.error('Error:', error);
    }

    setQuery(''); 
  };

  const fetchHistory = async () => {
    try {
      const res = await axios.get('/api/history'); 
      setFullHistory(res.data.history);
      setShowFullHistory(true); 
    } catch (err) {
      console.error('Error fetching history:', err);
    }
  };

  const clearHistory = async () => {
    try {
      await axios.post('/api/clear-history'); 
      setFullHistory([]); 
      setShowFullHistory(false); 
      setHistory([]); 
    } catch (err) {
      console.error('Error clearing history:', err);
    }
  };

  return (
    <div className="App">
      <h1>Chatbot</h1>
      <div className="header-buttons">
  <button onClick={() => {
    if (showFullHistory) {
      setShowFullHistory(false);
    } else {
      fetchHistory();
    }
  }}>
    {showFullHistory ? 'Hide Full History' : 'Show Full History'}
  </button>

  <button onClick={clearHistory}>Clear History</button>
</div>


      <div className="chat-container">
        <div className="chat-history">
          {history.map((entry, index) => (
            <div key={index} className={`chat-entry ${entry.sender}`}>
              <strong>{entry.sender === 'user' ? 'You' : 'AI'}:</strong>
              <p>{entry.text}</p>
            </div>
          ))}
        </div>
        <form onSubmit={handleSubmit} className="input-form">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask something..."
            required
          />
          <button type="submit">Send</button>
        </form>

        {showFullHistory && (
          <div className="chat-history full-history">
            <h2>Full History</h2>
            {fullHistory.map((entry, index) => (
              <div key={index} className={`chat-entry ${entry.sender}`}>
                <strong>{entry.sender === 'user' ? 'You' : 'AI'}:</strong>
                <p>{entry.text}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
