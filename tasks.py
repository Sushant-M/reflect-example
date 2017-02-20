from celery import Celery
import requests

app = Celery('tasks', broker='amqp://localhost//')

@app.task
def cowrks_task(image):

	url = 'http://54.145.171.212:8000/pipeline/full'

	path = 'test_images/' + image +'.png'

	data = open(path,'rb').read()
	headers = {'Content-Type': 'image/png'}

	response = requests.post(url,data = data, headers = headers)

	test = response.json()

	ret_val =  test['Found People']

	print ret_val

	return ret_val
