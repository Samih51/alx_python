"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.stdin.readline()
abc="qwerty"
print(type(abc))
print(type(url))

request = requests.get(url)
print(request.headers['X-Request-Id'])

#https://alu-intranet.hbtn.io/status   https://intranet.hbtn.io