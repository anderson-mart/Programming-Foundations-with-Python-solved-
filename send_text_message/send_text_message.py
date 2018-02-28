#Send Text Message miniproject
#Note: Python 3 code
#WARNING: As Twilio isn't aviable in my country for SMS this codes has not been properly tested
#		  although it should work in an aviable country

from twilio import rest

sid=ACa51688964a7b101e690c6f7bc5f71cae
token = #Your own token here
client = TwilioRestClient

message = client.sms.messages.create(body="Hola", to="" from_="")