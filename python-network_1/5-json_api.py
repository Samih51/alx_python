"""importing requests"""
import requests

"""importing sys"""
import sys

if len(sys.argv) > 1:
    letter = {"q" : sys.argv[1]}
else:
     letter = {"q" : ""}


request = requests.post( "http://0.0.0.0:5000/search_user" , data = letter )

try:
    data = request.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
