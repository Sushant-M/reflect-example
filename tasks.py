from celery import Celery
import requests

#creating an instance, broker is the rabbitmq server
#running on localhost
app = Celery('tasks', broker='amqp://localhost//')


@app.task
def cowrks_task(image):

	try:
		#base url
		url = 'http://54.145.171.212:8000/pipeline/full'

		#path to the image file
		path = 'test_images/' + str(image)

		#open the file in byte mode
		data = open(path, 'rb').read()

		#content headers
		headers = {'Content-Type': 'image/png'}

		#send the post request and get the response back
		response = requests.post(url, data=data, headers=headers)

		#convert to text form for printing, can be printed directly as well
		ret_val = response.text
		print (ret_val)
		return ret_val
	except requests.exceptions.RequestException as err:
		#if we couldn't get the result for whatever reason, print the error
		print (err, 'Could not retrieve data')
		return 'error'
