import React, { useEffect, useState } from 'react';

function ClubList() {
  const [clubs, setClubs] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/clubs/admin/clubs/')  // исправлено
      .then(response => {
        if (!response.ok) {
          throw new Error('Ошибка сети: ' + response.status);
        }
        return response.json();
      })
      .then(data => setClubs(data))
      .catch(error => setError(error.message));
  }, []);

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  if (!Array.isArray(clubs)) {
    return <div>Загрузка...</div>;
  }

  return (
    <div>
      <h1>Список клубов</h1>
      <ul>
        {clubs.map(club => (
          <li key={club.id}>{club.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ClubList;
