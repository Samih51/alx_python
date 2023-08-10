"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]


request = requests.get(url)
try:
    print(request.headers['X-Request-Id'])
except:
    pass
