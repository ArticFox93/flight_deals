from twilio.rest import Client

ACCOUNT_SID = "your twilio account sid"
AUTH_TOKEN = "your twilio auth token"
TWILLIO_VIRTUAL_NUMBER = "your twilio virtual number"
YOUR_NUMBER = "your number"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILLIO_VIRTUAL_NUMBER,
            to=YOUR_NUMBER,
        )
        print(message.sid)