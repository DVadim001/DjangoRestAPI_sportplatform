import React, { useEffect, useState } from 'react';

function EventsPage() {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/events/api/events/")
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        // Если в ответе есть .results — используй его
        setEvents(data.results || []);
      })
      .catch((err) => {
        console.error("Ошибка:", err);
        setError(err.message);
      });
  }, []);

  return (
    <div>
      <h2>Список событий</h2>
      {error && <p style={{ color: "red" }}>Ошибка: {error}</p>}
      <ul>
        {Array.isArray(events) && events.length > 0 ? (
          events.map((event) => (
            <li key={event.id}>
              <strong>{event.name}</strong> — {event.start_time}
            </li>
          ))
        ) : (
          <li>Нет доступных событий.</li>
        )}
      </ul>
    </div>
  );
}

export default EventsPage;
