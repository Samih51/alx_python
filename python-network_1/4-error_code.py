"""importing requests"""
import requests

"""importing sys"""
import sys

#url = sys.argv[1]
request = requests.get("https://alu-intranet.hbtn.io/status")
print(request.next)
"""
status = request.status_code

if ( status >= 400):
    print("Error code:",status)
else
"""