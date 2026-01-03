import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 20 }, // Naikkan ke 20 pengguna dalam 30 detik
        { duration: '1m', target: 20 },  // Bertahan di 20 pengguna selama 1 menit
        { duration: '10s', target: 0 },  // Turunkan ke 0
    ],
};

export default function () {
    // Ubah URL di bawah sesuai endpoint yang ingin diuji (v1 atau v2)
    let url = 'http://host.docker.internal:8000/v2/task';
    let res = http.get(url);
    
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
    sleep(1);
}