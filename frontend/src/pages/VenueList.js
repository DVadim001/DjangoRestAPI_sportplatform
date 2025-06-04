import React, { useEffect, useState } from 'react';

function VenueList() {
  const [venues, setVenues] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/venues/api/venues/')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => setVenues(data.results || []))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Места проведения</h1>
      {error && <p style={{ color: 'red' }}>Ошибка: {error}</p>}
      {venues.length === 0 ? (
        <p>Нет доступных мест проведения.</p>
      ) : (
        <ul>
          {venues.map((venue) => (
            <li key={venue.id}>{venue.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default VenueList;
