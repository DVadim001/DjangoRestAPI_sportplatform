import React, { useEffect, useState } from 'react';

function PaymentList() {
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/payments/api/payments/')
      .then(res => res.json())
      .then(data => setPayments(data))
      .catch(err => console.error('Ошибка при получении платежей:', err));
  }, []);

  return (
    <div>
      <h1>Список платежей</h1>
      <ul>
        {payments.length > 0 ? (
          payments.map(payment => (
            <li key={payment.id}>
              {payment.amount} — {payment.status} — {payment.date}
            </li>
          ))
        ) : (
          <li>Нет данных о платежах.</li>
        )}
      </ul>
    </div>
  );
}

export default PaymentList;
