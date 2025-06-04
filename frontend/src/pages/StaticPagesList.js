import React, { useEffect, useState } from 'react';

function StaticPagesList() {
  const [pages, setPages] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/pages/static-pages/')
      .then(response => response.json())
      .then(data => setPages(data))
      .catch(error => console.error('Ошибка при загрузке:', error));
  }, []);

  return (
    <div>
      <h2>Информационные страницы</h2>
      <ul>
        {pages.map(page => (
          <li key={page.id}>
            <strong>{page.title}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StaticPagesList;