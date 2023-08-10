"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]


request = requests.get(url)
print(request.headers['X-Request-Id'])

