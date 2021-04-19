#!/bin/bash

# Script to run django's migrate commands etc

# Why this script?
# When run with docker-compose up, the db container might not have been up
# When the web container is already up and trying to connect
# So wait for 10 secs and try to run the commands

sleep 10

python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py init_users