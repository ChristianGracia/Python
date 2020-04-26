import os

from twilio.rest import Client

account_sid = $acc
auth_token = $auth

client = Client(account_sid, auth_token)

client.messages.create(
    to='+4014505739',
    from_='+14012354705',
    body='hi'
)
