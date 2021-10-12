import http from 'k6/http';
import { check } from 'k6';

export let options = {
  vus: __ENV.vus,
  duration: __ENV.duration,
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95 percent of response times must be below 500ms
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
  },
};

export default function () {
    let res = http.get(__ENV.url);
    check (res, {
        'HTTP 200 OK': (r) => r.status == 200,
    });
}