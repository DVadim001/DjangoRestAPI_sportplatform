import React, { useEffect, useState } from 'react';


function UserStatus() {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');

    if (token) {
      fetch('http://127.0.0.1:8000/api/users/me/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(res => {
          if (!res.ok) {
            throw new Error('Ошибка авторизации');
          }
          return res.json();
        })
        .then(data => setUsername(data.username))
        .catch(() => setUsername(null));
    }
  }, []);

  return (
    <span style={{ color: 'white' }}>
      {username ? `Привет, ${username}` : 'Вы не вошли'}
    </span>
  );
}

export default UserStatus;
