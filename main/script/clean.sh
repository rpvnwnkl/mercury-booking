#!/bin/bash

#EXECUTE THE SCRIPT BY ROOT

#Remove old sqlite database
rm ~/workspace/mercury_booking/mercury_booking.db

#Syncronize database from django
python ~/workspace/mercury_booking/manage.py syncdb --noinput

#Migrate all data
#python ~/workspace/soloalberghi/manage.py migrate

#Load initial user datas
python ~/workspace/mercury_booking/manage.py loaddata ~/workspace/mercury_booking/main/fixtures/initial_user_data.json

# Run server
python ~/workspace/mercury_booking/manage.py runserver
