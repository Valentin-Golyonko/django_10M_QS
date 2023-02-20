Django performance test.

System:

- Ubuntu 22.04.2 LTS
- Python 3.10.6
- Gunicorn 20.1.0
- Locust 2.14.2
- DRF 3.14.0

Run req.:

- LIMIT_IN_USE = LIMIT_1K
- gunicorn -w 4 django_10M_QS.wsgi
- locust --headless -u 100 -r 20 -t 2m

Data:

| URL    |                    3.2.18 |                     4.1.7 |                     4.2b1 |
|:-------|--------------------------:|--------------------------:|--------------------------:|
| /v1/   | 707 ms (640 ms), 4.31 rps | 959 ms (650 ms), 4.28 rps | 771 ms (650 ms), 4.19 rps |
| /v2/   | 983 ms (720 ms), 3.94 rps | 852 ms (710 ms), 3.97 rps | 858 ms (720 ms), 3.89 rps |
| /v3/   | 481 ms (385 ms), 7.17 rps | 466 ms (386 ms), 7.02 rps | 458 ms (390 ms), 7.07 rps |
| /v3_2/ | 400 ms (380 ms), 7.24 rps | 410 ms (385 ms), 7.10 rps | 463 ms (390 ms), 6.97 rps |
| /v3_3/ |                         - | 465 ms (385 ms), 7.16 rps | 464 ms (390 ms), 7.07 rps |
| /v4/   | 464 ms (385 ms), 7.23 rps | 468 ms (390 ms), 7.10 rps | 535 ms (395 ms), 7.14 rps |
| /v5/   | 466 ms (385 ms), 7.30 rps | 494 ms (390 ms), 7.19 rps | 437 ms (385 ms), 7.11 rps |
| -      |                         - |                         - |                         - |

description '/v1/':
771 ms = Locust Min GET time
(650 ms) = Postman Avg GET time
4.19 rps = Locust req/s

