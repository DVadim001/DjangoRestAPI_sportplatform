import React, { useEffect, useState } from 'react';
import { fetchWithAuth } from '../utils/fetchWithAuth';

function EquipmentList() {
  const [equipment, setEquipment] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchWithAuth('/api/equipment/')
      .then(res => {
        if (!res.ok) {
          throw new Error('Ошибка загрузки: ' + res.status);
        }
        return res.json();
      })
      .then(data => setEquipment(data.results || data))
      .catch(err => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Инвентарь</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {equipment.map(item => (
          <li key={item.id}>{item.name} — {item.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default EquipmentList;
