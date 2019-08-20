import requests


def client():
    credentials = {"username": "test2", "password": "NotagoodP@ssword"}

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)
    token_h = "Token " + response_data['key']
    print(token_h)
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print(response.json())



if __name__ == "__main__":
    client()