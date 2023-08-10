"""importing requests"""
import requests

"""importing sys"""
import sys

username = sys.argv[1]
password = sys.argv[2]
request = requests.get('https://api.github.com/user', auth=(username, password))
data = request.json()
print(data.get('id'))