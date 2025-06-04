import React, { useEffect, useState } from 'react';

function MessageList() {
  const [messages, setMessages] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/communication/api/messages/')
      .then(res => {
        if (!res.ok) throw new Error('Ошибка запроса: ' + res.status);
        return res.json();
      })
      .then(data => setMessages(data.results || []))
      .catch(err => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Список сообщений</h1>
      {error && <p style={{ color: 'red' }}>Ошибка: {error}</p>}
      {messages.length === 0 ? (
        <p>Нет сообщений.</p>
      ) : (
        <ul>
          {messages.map(msg => (
            <li key={msg.id}>
              <strong>{msg.subject}</strong> от {msg.sender_username} — {msg.sent_at}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default MessageList;
