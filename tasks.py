from celery import Celery
import requests

app = Celery('tasks', broker='amqp://localhost//')


@app.task
def cowrks_task(image):

	try:
		url = 'http://54.145.171.212:8000/pipeline/full'
		path = 'test_images/' + str(image)
		data = open(path, 'rb').read()
		headers = {'Content-Type': 'image/png'}
		response = requests.post(url, data=data, headers=headers)
		ret_val = response.text
		print (ret_val)
		return ret_val
	except requests.exceptions.RequestException as err:
		print (err, 'Could not retrieve data')
		return 'error'
