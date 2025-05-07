from twilio.rest import Client     # Import Twilio REST client library

account_sid = 'AC9807f1a9e1c43993ba857e0eca76a8b1'
auth_token  = '64f8b665e15ee3af12e9fc938610dfed'

client = Client(account_sid, auth_token)
# Instantiate the Twilio client with your Account SID and Auth Token

FROM_NUMBER = '+16085645045'      # Your Twilio phone number (sender)
TO_NUMBER   = '+17205619733'      # Destination phone number (recipient)

def send_text(body="Motion Detected!"):
    message = client.messages.create(
        body=body,                # Text content of the message
        from_=FROM_NUMBER,        # Sender number
        to=TO_NUMBER              # Recipient number
    )
    print(f"Text sent: {message.sid}")  # Print the Message SID for confirmation
