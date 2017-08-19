# USING AN API WITH PYTHON
# requests library documentation is here: https://www.python-requests.org/en/latest
# this tutorial is based on the Python API tutorial by Vik Paruchuri 
# at https://www.dataquest.io/blog/python-api-tutorial
# we're using the Open Notify API (information about the International Space Station)
# API documentation at http://www.open-notify.org/Open-Notify-API/

import requests

response = requests.get("http://api.open-notify.org/iss-now.json)
print (response.status_code)

# 200 is good! 

response = requests.get("http://api.open-notify.org/iss-now")
print (response.status_code)

 # 404 means it can't find anything ...
 
response = requests.get("http://api.open-notify.org/iss-pass.json")
print (response.status_code)

# 400 means it needs more information, like some parameters

response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")

data = response.content

print (data)
print (type(data))

# ---------------------------------------------------------------------------------------

import json

# json.loads takes in a json string and turns it into a python object

data_dict = json.loads(data)
print (type(data_dict))

# json.dumps takes in a python object and turns it into a string

data_string = json.dumps(data_dict)
print (type(data_string))

# ---------------------------------------------------------------------------------------

print (response.headers)

print (response.headers['content-type])

# ---------------------------------------------------------------------------------------

response = requests.get("http://api.open-notify.org/astros.json")

data = response.json()

print (data)

print (data["number"])






