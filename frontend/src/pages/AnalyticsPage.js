import React, { useEffect, useState } from 'react';

function AnalyticsPage() {
  const [pageVisits, setPageVisits] = useState([]);
  const [userActions, setUserActions] = useState([]);

  useEffect(() => {
    // Загрузка данных посещений
    fetch('http://127.0.0.1:8000/api/analytics/pagevisits/')
      .then(res => res.json())
      .then(data => setPageVisits(data))
      .catch(err => console.error('Ошибка при загрузке посещений:', err));

    // Загрузка действий пользователей
    fetch('http://127.0.0.1:8000/api/analytics/useractions/')
      .then(res => res.json())
      .then(data => setUserActions(data))
      .catch(err => console.error('Ошибка при загрузке действий пользователей:', err));
  }, []);

  return (
    <div>
      <h1>Аналитика</h1>

      <section>
        <h2>Посещения страниц</h2>
        <ul>
          {pageVisits.map((visit, index) => (
            <li key={index}>
              {visit.page} — {visit.visit_count || visit.id} посещений
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Действия пользователей</h2>
        <ul>
          {userActions.map((action, index) => (
            <li key={index}>
              Пользователь {action.user} — {action.action_type} на {action.page} ({action.timestamp})
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default AnalyticsPage;
