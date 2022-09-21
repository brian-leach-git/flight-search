import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUM = os.environ.get('TWILIO_PHONE_NUM')


class NotificationManager:
    """Sends text notifications to users"""

    def send_text(self, notif_info, phone_num_list):
        """Takes the list of notification info and a list of user phone
        numbers and sends 1 text to each user per cheap flight"""

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # do not send any texts if there are no cheap flights
        if len(notif_info) > 0:

            for number in phone_num_list:

                for flight in notif_info:
                    text = f'''
                    🚨Cheap flight alert🚨
                    Only ${flight['price']} to fly ROUND TRIP from {flight['departureCity']}-{flight['departureAirport']} to {flight['arrivalCity']}-{flight['arrivalAirport']} from {flight['startDate']} to {flight['endDate']}
                    '''

                    # send text
                    client.messages.create(body=text, from_=TWILIO_PHONE_NUM, to=number)


