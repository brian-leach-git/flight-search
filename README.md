# Flight-Search
A personal project meant to search for abnormally cheap flights out of Seattle to interesting destinations.

A Google Sheet is used as the database for cities of interest and user information. All flights are currently presumed to fly out of Seattle with a maximum of 1 layover. Users will be texted with a customer message per flight for each round-trip itinerary that falls below the maximum allowable price for that destination.

This project uses the following APIs:
  Sheety - used for communicating with a Google Sheet tables.
  Kiwi Tequila - used for searching for locations and flights.
  Twilio - used to send SMS to users.
