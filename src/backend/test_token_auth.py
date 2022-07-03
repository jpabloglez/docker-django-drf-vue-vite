import requests


def client():
    credentials = {'username': 'admin@admin.com', 'password': 'admin'}
    response = requests.post('http://localhost:8000/api/rest-auth/login/', data=credentials)

    print(" - Response:", response.status_code)
    data = response.json()
    print(" - Data:", data)


if __name__ == '__main__':
    client()