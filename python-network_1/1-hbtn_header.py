"""importing sys"""
import sys

"""importing requests"""
import requests


url = input()

request = requests.get(url)
print(request.headers['X-Request-Id'])

#https://alu-intranet.hbtn.io/status   https://intranet.hbtn.io