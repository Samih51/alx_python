"""importing requests"""
import requests

"""importing sys"""
import sys

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""


request = requests.post( "http://0.0.0.0:5000/search_user" , data = {'letter':q} )
print()
try:
    data = request.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
