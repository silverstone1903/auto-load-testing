# https://github.com/amitvkulkarni/Build-ML-Models-As-Rest-API/blob/main/Locust/perf.py

import time
import json
from locust import HttpUser, task, between
import random

users = ['17850', '13047', '12583', '13748', '15100',
         '15291', '14688', '17809', '15311', '16098']
items = ['85123A', '71053', '84406B', '84029G', '84029E',
         '22752', '21730', '22633', '22632', '84879']

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json'}


class HealthCheck(HttpUser):
    wait_time = between(10, 15)
    host = 'http://localhost:8000'

    @task
    def test_hc(self):
        self.client.get("/", headers=headers)


class Reco(HttpUser):
    # host = 'http://localhost:8000'

    @task(5)
    def test_user(self):
        user = int(random.choice(users))

        self.client.get(
            "/predict/user/{0}".format(user))

    @task(5)
    def test_item(self):
        item = random.choice(items)

        self.client.get(
            "/predict/item/{0}".format(item))
