import React, { useEffect, useState } from 'react';

function ScheduleList() {
  const [schedules, setSchedules] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/schedules/api/schedules/')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Ошибка HTTP: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => setSchedules(data.results || []))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Расписания</h1>
      {error && <p style={{ color: 'red' }}>Ошибка: {error}</p>}
      {schedules.length === 0 ? (
        <p>Нет доступных расписаний.</p>
      ) : (
        <ul>
          {schedules.map((s) => (
            <li key={s.id}>
              <strong>{s.title}</strong> — {s.start_time} до {s.end_time}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ScheduleList;
