export async function fetchWithAuth(url, options = {}) {
  const token = localStorage.getItem('access_token');

  const headers = {
    ...(options.headers || {}),
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json',
  };

  const response = await fetch(url, {
    ...options,
    headers,
  });

  // Обработка 401 (неавторизован)
  if (response.status === 401) {
    console.error('Токен недействителен или истёк. Переавторизация.');
    // Можешь добавить редирект на login или очистку токенов тут
  }

  return response;
}
