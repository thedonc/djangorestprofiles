import requests


def client():
    data = {
        "username": "test3",
        "email": "test@test.com",
        "password1": "NotagoodP@ssword",
        "password2": "NotagoodP@ssword"
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()