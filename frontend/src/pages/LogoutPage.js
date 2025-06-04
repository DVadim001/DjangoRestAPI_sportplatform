import React, { useEffect } from 'react';

function LogoutPage() {
  useEffect(() => {
    // Удаляем токен
    localStorage.removeItem('token');

    // Через 2 секунды перенаправим на главную
    const timer = setTimeout(() => {
      window.location.href = '/';
    }, 2000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div>
      <h2>Вы вышли из системы</h2>
      <p>Возврат на главную страницу...</p>
    </div>
  );
}

export default LogoutPage;
