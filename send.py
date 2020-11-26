import requests
import json

def send_sms(number, message):
	url = 'https://www.fast2sms.com/dev/bulk'
	para = {
	'authorization' = '# Your Fast2SMS authorization key'
	'sender_id' = 'FSTSMS'
	'language' = 'english'
	'route' = 'p'
	'message' = message
	'numbers' = number
	'flash' = "1"
	}

number = input('Enter your number : ')
message = input('Enter your message : ')
send_sms(number, message)
