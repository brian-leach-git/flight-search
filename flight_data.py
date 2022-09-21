from datetime import datetime

class FlightData:
    """Structures the flight data from the FlightSearch object.

    Attributes:
        max_price_dict: Dictionary of IATA code: maximum price.
        cheap_flights: list of only flights that are below their maximum price.
        notification_info: a list of dictionaries containing info about each flight.
    """

    def __init__(self):
        """Inits notification_info as an empty list and the rest as None."""

        self.max_price_dict = None
        self.cheap_flights = None
        self.notification_info = []

    def condense_data(self):
        """Simplifies flight data and prepares the notification_info attribute."""

        for flight in self.cheap_flights:

            start_time = flight['route'][0]['dTimeUTC']
            start_date = datetime.fromtimestamp(int(start_time)).strftime('%m/%d/%Y')
            end_time = flight['route'][-1]['aTimeUTC']
            end_date = datetime.fromtimestamp(int(end_time)).strftime('%m/%d/%Y')

            self.notification_info.append({
                'price': flight['price'],
                'startDate': start_date,
                'endDate': end_date,
                'departureAirport': flight['flyFrom'],
                'departureCity': flight['cityFrom'],
                'arrivalAirport': flight['flyTo'],
                'arrivalCity': flight['cityTo']
            })

    def check_price(self, flight_data, price_dict):
        """Filters out any flights that are not cheaper than their max price."""
        # takes the full flight data and dictionary of max prices and sets attribute with only flights below max price

        data = flight_data['data']
        self.cheap_flights = data
        self.max_price_dict = price_dict

        for flight in data:

            max_price = self.max_price_dict[flight['cityCodeTo']]
            price = flight['price']

            if price > max_price:
                self.cheap_flights.remove(flight)

        self.condense_data()


