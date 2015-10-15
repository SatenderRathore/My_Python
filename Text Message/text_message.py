from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC86e2b6e3bbfed0ee4597bc0e9950568a1"
auth_token  = "14de612aa32030bd769ca1fee8bee1781"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hare Krishna :) :) ",
    to="+9181285024511",    # Replace with your phone number
    from_="+131567542531") # Replace with your Twilio number
print message.sid
