"""
site: https://locust.io/
git: https://github.com/locustio/locust
doc: http://docs.locust.io/en/stable/

Before run:
    - pip install -U locust gunicorn
    - ! IMPORTANT: backend server should run in Docker with uWSGI / Gunicorn !
    - gunicorn -w 4 django_10M_QS.wsgi

run v1:
    locust
run v2:
    locust --headless -u 100 -r 20 -t 2m
"""
import logging

from locust import HttpUser, task
from requests import Response
from requests.exceptions import JSONDecodeError

logger = logging.getLogger(__name__)


class LocustRPS(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_start(self):
        pass

    @task
    def endpoints_test(self) -> None:
        # target_url = "/v1/"
        # target_url = "/v2/"
        # target_url = "/v3/"
        # target_url = "/v3_2/"
        target_url = "/v3_3/"
        # target_url = "/v4/"
        # target_url = "/v5/"

        self.universal_page(target_url=target_url)
        return None

    """ ------------------ request utilities -> ------------------ """

    def universal_page(self, target_url: str) -> None:
        response: Response = self.client.get(url=target_url)

        if (status_code := response.status_code) != 200:
            logger.error(f"universal_page(): status_code != 200;" f" {status_code = }")
            if response.status_code == 0:
                return None
            response_data = self.response_json(response)
        return None

    @staticmethod
    def response_json(response: Response) -> dict:
        try:
            return response.json()
        except JSONDecodeError:
            msg = f"response_json(): JSONDecodeError; {response.url = };"
            logger.error(msg)
        except Exception as ex:
            msg = f"response_json(): response.json() Ex; {response.url = }; {ex = }"
            logger.error(msg)
        return {}

    """ ------------------ <- request utilities ------------------ """
