import React, { useEffect, useState } from 'react';

function UsersPage() {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/users/profile/")
      .then((res) => res.json())
      .then((data) => setProfiles(data))
      .catch((err) => console.error("Ошибка:", err));
  }, []);

  return (
    <div>
      <h2>Список профилей пользователей</h2>
      <ul>
        {profiles.map((p) => (
          <li key={p.id}>{p.user}</li>
        ))}
      </ul>
    </div>
  );
}

export default UsersPage;
