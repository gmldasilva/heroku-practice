import os
import requests
from pytest_steps       import test_steps

url = f"http://{os.environ['DOCKER_HOST_ADDRESS']}:{str(3000)}"

@test_steps('test_create_new_user')
def test_authorization():
    endpoint = f'{url}/authentication'
    response = requests.request("POST", endpoint, json={
        "user":"Gabriel",
        "credential":"jsaisjiajsi"
    })
    assert response.status_code == 200
    yield
