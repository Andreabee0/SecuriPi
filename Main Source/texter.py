from twilio.rest import Client     # Import Twilio REST client library

account_sid = 'AC9807f1a9e1c43993ba857e0eca76a8b1'
auth_token  = 'foo' #I cant have my token on a public website, but the code on the Pi contains the actual token

client = Client(account_sid, auth_token)
# Instantiate the Twilio client with my Account SID and Auth Token

FROM_NUMBER = '+16085645045'      # Twilio phone number (sender)
TO_NUMBER   = '+17205619733'      # Destination phone number (recipient)

def send_text(body="Motion Detected!"):
    message = client.messages.create(
        body=body,                # Text content of the message
        from_=FROM_NUMBER,        # Sender number
        to=TO_NUMBER              # Recipient number
    )
    print(f"Text sent: {message.sid}")  # Print the Message SID for confirmation
