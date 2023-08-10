"""importing requests"""
import requests

"""importing sys"""
import sys

q = sys.argv[1]

if q== None:
    q=""
request = requests.post( "http://0.0.0.0:5000/search_user" , data = {'letter':q} )
 
print(dir(request))
