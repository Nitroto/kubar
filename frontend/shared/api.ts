let API_HOST;


const url = '';

const prodDatabase = false;
const hostname = window && window.location && window.location.hostname;

if (hostname === url || prodDatabase) {
    API_HOST = 'https://' + url;
} else {
    API_HOST = 'http://127.0.0.1:8000';
}

export { API_HOST };
