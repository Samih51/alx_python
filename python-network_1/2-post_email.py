"""importing requests"""
import requests

"""importing sys"""
import sys

url = sys.argv[1]
email = sys.argv[2]

request = requests.post( url , data = {'email':email} )
#response = request.json()
#print("Your email is:", response.get("form")['email'])

print("Response content:", request.text)  # Print the response content

try:
    response = request.json()
    print("Your email is:", response.get('email'))
except Exception as e:
    print("Error:", e)
