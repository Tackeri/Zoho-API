
import requests



url = 'https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE=ZohoCRM/crmapi&EMAIL_ID=scottdminter@gmail.com&PASSWORD=wedge753&DISPLAY_NAME=Testing3'

response = requests.post(url)
print (response)
print (response.headers)
print (response.text)