import React, { useEffect, useState } from 'react';

function ResultList() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/results/api/results/')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Ошибка при загрузке данных: ' + res.status);
        }
        return res.json();
      })
      .then((data) => setResults(data.results || []))
      .catch((err) => console.error('Ошибка загрузки результатов:', err));
  }, []);

  return (
    <div>
      <h1>Результаты</h1>
      {results.length === 0 ? (
        <p>Результаты пока отсутствуют.</p>
      ) : (
        <ul>
          {results.map((result) => (
            <li key={result.id}>
              <strong>{result.user}</strong>: {result.score}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ResultList;
