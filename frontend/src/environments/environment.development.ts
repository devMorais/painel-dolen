export const environment = {
  production: false,
  apiUrl: (typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'))
    ? 'http://127.0.0.1:8000/api'
    : 'https://backend.test/api',
};