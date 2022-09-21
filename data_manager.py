import requests
import os

PRICES_URL = os.environ.get('PRICES_URL')
USERS_URL = os.environ.get('USERS_URL')

class DataManager:
    """Communicates with Google Sheet.

    Uses Sheety API to query and insert data into the Google sheet.

    Attributes:
        city_list: A list of full-length city names as strings.
        min_prices: A dictionary with IATA code keys and minimum price int values.
        phone_nums: A list of formatted user phone number
    """

    def __init__(self):
        """Inits DataManager with blank attributes."""

        self.city_list = None
        self.min_prices = None
        self.phone_nums = None

    def get_cities(self):
        """Queries Google Sheet and sets city_list."""
        print(PRICES_URL)
        print(os.environ.get('PRICES_URL'))
        request = requests.get(url=PRICES_URL)
        data = request.json()

        self.city_list = [row['city'] for row in data['prices']]

    def post_codes(self, codes):
        """Takes a list of IATA codes and adds them to the Google Sheet."""

        index = 2

        for code in codes:

            param_dict = {"price": {
                'iataCode': code}}

            request_url = f'{PRICES_URL}/{index}'
            requests.put(url=request_url, json=param_dict)

            index += 1

    def get_prices(self):
        """Queries the Google sheet and builds the min_prices dictionary"""
        request = requests.get(url=PRICES_URL)
        data = request.json()

        self.min_prices = {row['iataCode']: row['lowestPrice'] for row in data['prices']}

    def get_users(self):
        """Queries the Google Sheet and generates a
        list of formatted user phone numbers"""
        request = requests.get(url=USERS_URL)
        data = request.json()

        self.phone_nums = [f"+1{i['phoneNumber']}" for i in data['users']]
