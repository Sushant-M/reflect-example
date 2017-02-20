# To execute: sudo bash start.sh
sudo rabbitmq-server

celery worker -A tasks
