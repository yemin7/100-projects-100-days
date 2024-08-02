from twilio.rest import Client


class SendSMS:

    def __init__(self, sid, token, sender, receiver):
        self.sid = sid
        self.token = token
        self.sender = sender
        self.receiver = receiver

    def send(self, message):
        client = Client(self.sid, self.token)
        message = client.messages.create(from_=self.sender, to=self.receiver, body=message)
        print(message.sid)
        print(message.status)
