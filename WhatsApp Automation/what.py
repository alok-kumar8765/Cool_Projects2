from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid,auth_token)

def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Hello",
        to='whatsapp:+15555555555'
    )
    print(message.sid)


# ref link ; https://www.youtube.com/watch?v=pQeFxdT3FGY&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=38