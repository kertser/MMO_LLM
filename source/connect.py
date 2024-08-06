import requests
from config import TOKEN_PATH, BASE_URL
import json

class APIClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(APIClient, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, url=BASE_URL):
        if self.__initialized:
            return
        self.__initialized = True

        # Initialize token
        self.TOKEN = self.load_token()
        if self.TOKEN is None:
            raise ValueError("Failed to load token.")

        self.base_url = url
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

    @staticmethod
    def load_token():
        """Load the token from a JSON file."""
        try:
            with open(TOKEN_PATH, 'r') as file:
                data = json.load(file)
                return data.get("token")
        except FileNotFoundError:
            print(f"Error: The file {TOKEN_PATH} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {TOKEN_PATH} contains invalid JSON.")
        return None

    def get(self, endpoint, params=None):
        """Get the status from a specific endpoint."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return self.handle_response(response)

    def post(self, endpoint, data=None):
        """Post the command to the API endpoint."""
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

# Create a singleton instance of APIClient
client = APIClient()