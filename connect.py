import requests
from config import TOKEN_PATH, BASE_URL
import json

class APIClient:

    def __init__(self, url=BASE_URL):
        """ connecting to the API """

        # read token:
        with open(TOKEN_PATH, "r") as f:
            self.TOKEN = f.read().strip()
            f.close()

        self.base_url = url
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }


    def get(self, endpoint, params=None):
        """ Getting the status from specific endpoint """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)

        return self.handle_response(response)

    def post(self, endpoint, data=None):
        """ post the command into API endpoint """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)

        return self.handle_response(response)

    def handle_response(self, response):
        """Handle the HTTP response, checking for errors."""
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None






