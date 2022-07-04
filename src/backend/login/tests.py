from django.test import TestCase

# Create your tests here.
import requests


def client():
    credentials = {'username': 'admin@admin.com', 'password': 'admin'}
    response = requests.post('http://localhost:8000/login/', data=credentials)

    print(" - Response status code:", response.status_code)
    data = response.json()
    print(" - Response data:", data)


if __name__ == '__main__':
    client()