import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import os

TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')
TEQUILA_URL = 'https://api.tequila.kiwi.com/'


class FlightSearch:
    """Communicates with flight Search API.

    Uses Kiwi Tequila API to find information about locations and flights.

    Attributes:
        iata_codes: A list of IATA codes that sequentially correspond to the city list.
        flight_data: Full JSON response from flight search API.
    """

    def __init__(self):
        """Inits FlightSearch with iata_codes as an empty list and flight_data as None."""

        self.iata_codes = []
        self.flight_data = None

    def get_codes(self, cities):
        """Gets a list of IATA codes from a list of city names."""

        header_dict = {'apikey': TEQUILA_API_KEY}

        for city in cities:
            param_dict = {'term': city,
                          'location_types': 'city',
                          'limit': 1,
                          'active_only': True}
            request = requests.get(url=TEQUILA_URL + 'locations/query', headers=header_dict, params=param_dict)
            data = request.json()
            code = data['locations'][0]['code']

            self.iata_codes.append(code)

    def search_flights(self):
        """Searches for flights and populates flight_data attribute.

        Search flights in the next 6 months from SEA to each of the cities
        in the Google Sheet. Search parameters are listed in param_dict.
        """
        # Searches for flights in the next 6 months for each IATA code

        today = date.today()
        today_date = today.strftime("%d/%m/%Y")
        six_months = date.today() + relativedelta(months=+6)
        end_date = six_months.strftime("%d/%m/%Y")
        city_string = ','.join(self.iata_codes)

        param_dict = {'fly_from': 'SEA',
                      'fly_to': city_string,
                      'date_from': today_date,
                      'date_to': end_date,
                      'nights_in_dst_from': 5,
                      'nights_in_dst_to': 10,
                      'flight_type': 'round',
                      'one_for_city': 1,
                      'curr': 'USD',
                      'max_stopovers': 1
                      }

        request = requests.get(url=f"{TEQUILA_URL}search", params=param_dict, headers={'apikey': TEQUILA_API_KEY})
        data = request.json()

        self.flight_data = data
