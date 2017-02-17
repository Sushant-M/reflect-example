# reflect-example
Reflect's public api usage with RabbitMQ and Celery


### API explained
Reflect is the facerecognition API exposed for public by CoWrks. API end points are available for training faces and recognize the faces based on trained faces. Training API is not yet established but recognition can be done by hitting http://54.145.171.212:8000/pipeline/full with 'Content-Type' headers set to 'image/png' and pass the image.


#### TODO - Develop a system that uses RabbitMQ and Celery
We use RabbitMQ and Celery for queuing the tasks. API end point would take around 4 second to return the result. As the number of images increase, after requesting API end point, each one should go to the queue and wait for the API reply
