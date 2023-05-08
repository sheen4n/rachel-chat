import axios from 'axios';

// http.js
const getBaseUrl = () => {
  // let url;
  // switch(process.env.NODE_ENV) {
  //   case 'production':
  //     url = 'https://stackoverflow.com';
  //     break;
  //   case 'development':
  //   default:
  //     url = 'https://google.com';
  // }
  const url = 'http://localhost:8000';
  return url;
};

const http = axios.create({
  baseURL: getBaseUrl(),
});

export default http;
