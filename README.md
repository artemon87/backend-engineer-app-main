# Syndio Backend App

## Setup 
###### MAC instructions
#### Virtual environment

##### Install your own virtual environment
* Install ```python 3.9.13``` (other python3 virsions should work as well)
* Install ```virtualenv``` module 
* To install your own virtual environment use ```virtualenv -p python3 ve```
* To activate newly installed ve run ```source ve/bin/activate```
* Install dependencies by running ```pip install -r requirements.txt``` inside project folder (backend-engineering...)
* Done

##### Use an existing virtualenv
* To activate an existing ve run ```source ve/bin/activate``` inside project folder (backend-engineering...)
* Done (If failed please use **Install your own virtual environment** guide)

# To run the script

* Navigate to *api* folder ```cd api``` and run ```python app.py``` to start *Flask* web app
* To change app's port number or host IP address navigate to ```config.py``` (inside *api* directory).