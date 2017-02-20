import requests
import json

def cowrks_task():
	url = 'http://54.145.171.212:8000/pipeline/full'

	data = open('1.png','rb').read()
	headers = {'Content-Type': 'image/png'}

	response = requests.post(url,data = data, headers = headers)

	test = response.json()

	print test['Found People']

	return response.json()

if __name__ == '__main__':
	ans = cowrks_task()
	print ans