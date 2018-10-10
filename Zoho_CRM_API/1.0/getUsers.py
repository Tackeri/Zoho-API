


import requests, json
import credentials


url = 'https://crm.zoho.com/crm/private/xml/Users/getUsers?{token}&scope=crmapi&type=ActiveUsers'
url = url.replace('{token}', credentials.token)
response = requests.get(url)
# jsonData = json.loads(response.text)
# print (json.dumps(jsonData, sort_keys=True, indent=4))
print (response.text)