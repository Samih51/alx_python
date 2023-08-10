"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]


request = requests.get(url)
if request.headers['X-Request-Id']:
    print(request.headers['X-Request-Id'])

