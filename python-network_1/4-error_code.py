"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]
#request = requests.get("https://alu-intranet.hbtn.io/status")

request = requests.get(url)
status = request.status_code
if status >= 400:
    print("Error code: {}".format(status))
else:
    print("Regular request")