#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-pip
sudo apt-get install -y build-essential python-dev
# sudo pip install flask
# sudo python -m pip install pymongo
# sudo pip install Flask-MongoKit

# sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
# echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list

# sudo apt-get update
# sudo apt-get install -y mongodb-10gen

# sudo service mongodb start
sudo pip install django
sudo pip install django-bootstrap3
sudo pip install sendgrid
