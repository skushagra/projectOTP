import requests
import json

def send_sms(number, message):
	url = 'https://www.fast2sms.com/dev/bulk'
	para = {
	'authorization' = '0akrzRopPTJV9OHENKxfyMctuZeqUbSG7DdF6Xg1C3IQ8BAhYm0snNVvCpIWU4S9YBj7M85qQkDt2yzF'
	'sender_id' = 'FSTSMS'
	'language' = 'english'
	'route' = 'p'
	'message' = "This is a test flash message!"
	'numbers' = '7018487271'
	'flash' = "1"
	}