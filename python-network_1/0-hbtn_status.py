"""importing requests"""
import requests
request = requests.get("https://alu-intranet.hbtn.io/status")
print("- type:",type(request) )
print("- content:",request.reason)