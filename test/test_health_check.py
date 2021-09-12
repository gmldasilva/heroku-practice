import os
import requests
from pytest_steps       import test_steps

url = f"http://{os.environ['DOCKER_HOST_ADDRESS']}:{str(3000)}"

@test_steps('test_health_check')
def test_health_check():
    endpoint = f'{url}/'
    response = requests.request("GET", endpoint)
    assert response.status_code == 200
    yield

    endpoint = f'{url}/aaa'
    response = requests.request("GET", endpoint)
    assert response.status_code == 200
    yield