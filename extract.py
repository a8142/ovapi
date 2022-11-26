import requests


def get_ovapi_line_data(url: str) -> dict:
    response = requests.get(url)
    return response.json()
