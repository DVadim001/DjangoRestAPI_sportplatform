import React, { useEffect, useState } from 'react';

function RegistrationList() {
  const [registrations, setRegistrations] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/registrations/api/registrations/')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => setRegistrations(data.results || data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Список регистраций</h1>
      {error && <p>Ошибка: {error}</p>}
      {!registrations.length ? (
        <p>Нет доступных регистраций.</p>
      ) : (
        <ul>
          {registrations.map((reg) => (
            <li key={reg.id}>
              Событие ID: {reg.event} | Пользователь ID: {reg.user}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default RegistrationList;
