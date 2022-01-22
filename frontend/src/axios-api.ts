import axios from "axios";

const getAPI = axios.create({
  baseURL: "api/",
  timeout: 10000,
});

export { getAPI };
