"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.stdin.readline()


request = requests.get(url)
print(request.headers['X-Request-Id'])

