"""importing requests"""
import requests

"""importing sys"""
import sys

request = requests.get(sys.argv[1])
if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
else:
        print(request.text)