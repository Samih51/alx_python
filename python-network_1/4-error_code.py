"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]

request = requests.get(url)

if request.status_code >= 400:
    print("Error code: {}".format(request.status_code))
else:
    print("Regular request")