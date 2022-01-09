import axios from "axios";

const getAPI = axios.create({
  baseURL: "http://localhost:8000/v1",
  timeout: 1000,
});

export { getAPI };
