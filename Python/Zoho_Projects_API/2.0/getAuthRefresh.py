__author__ = 'MinterS'

# Refresh Access Token with Refresh Token from tokens.py
# Collects user and client details from credentials.py
# Calls the Auth API to return Access Token to file

from Authentication import tokens, credentials
from Resources import statusCodes
import requests
import json


def getAuthRefresh():
    # Collect Refresh Token and Build URL
    url = 'https://accounts.zoho.com/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token'
    url = url.replace("{refresh_token}", tokens.getRefresh())
    url = url.replace("{client_id}", credentials.client_id)
    url = url.replace("{client_secret}", credentials.client_secret)

    # Call API and Return Status
    response = requests.post(url)
    status = response.status_code
    message = statusCodes.statusCode(status)

    # Print Input Data
    print('')
    print('---- Request ----')
    print('URL:', url)

    # Parse Response data
    json_data = json.loads(response.text)
    try:
        error = json_data["error"]
    except:
        error = 'None'
    try:
        access = json_data["access_token"]
    except:
        access = 'No Token'

    # Print Output Data
    print('')
    print('---- Response ----')
    if error != 'None':
        print('Error:', error)
        print(response)
        print(response.text)
    else:
        print('Access:', access)
        # Write Token to File
        tokens.saveAccess(access)


token = getAuthRefresh()
