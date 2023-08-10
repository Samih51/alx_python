"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]
email = sys.argv[2]

request = requests.post( url , data = {'email':email} )

print(request.text)
