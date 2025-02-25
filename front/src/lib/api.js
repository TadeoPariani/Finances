import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // URL del backend Django
  withCredentials: true, // Enviar cookies de sesión
});

export default api;
