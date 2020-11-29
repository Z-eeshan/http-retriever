# Retrieving Homepage using Python

import requests
#Vulnerable is pointing to a webpage hosted using apache webserver on Ubuntu VM
r =requests.get('http://vulnerable')
print("Request Status Code {}" r.status_code)
print("HTML Response {}" r.text)
