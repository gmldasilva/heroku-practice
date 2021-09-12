import os
import requests
from pytest_steps       import test_steps

@test_steps('test_health_check')
def test_health_check():
    endpoint = '/'
    url = f"http://{os.environ['DOCKER_HOST_ADDRESS']}:{str(3000)}{endpoint}"
    response = requests.request("GET", url)
    assert response.status_code == 200
    yield

    endpoint = '/aaa'
    url = f"http://{os.environ['DOCKER_HOST_ADDRESS']}:{str(3000)}{endpoint}"
    response = requests.request("GET", endpoint)
    assert response.status_code == 200
    yield