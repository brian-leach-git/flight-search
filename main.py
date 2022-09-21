"""This program uses 3 APIs to search for cheap flights and text our users to alert them of good deals"""

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


dm = DataManager()

# Get a list of cities and their max prices from our Google sheet.
dm.get_cities()

# Get a list of our users formatted phone numbers from the Google sheet.
dm.get_users()

fs = FlightSearch()

# Use flight search API to get a list of IATA codes based on the cities listed in the Google sheet.
fs.get_codes(dm.city_list)

# Post the IATA codes onto the Google sheet so that they can be read going forward.
dm.post_codes(fs.iata_codes)

dm.get_prices()

# Search flights to all destinations and save the full json response as an attribute.
fs.search_flights()

fd = FlightData()

# Check if the price for each flight is lower than our max price, then drop all flights that are not cheap enough.
# Reformat the data for each flight into an easily searchable dictionary
fd.check_price(fs.flight_data, dm.min_prices)

nm = NotificationManager()

# Send our cheap flight text to each user.
nm.send_text(fd.notification_info, dm.phone_nums)
