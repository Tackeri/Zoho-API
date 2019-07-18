__author__ = "MinterS"

import requests, json

def main():
    # Define Parameters
    url = 'https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE={Scope}&EMAIL_ID={UsernameEmailID}&PASSWORD={Password}&DISPLAY_NAME={ApplicationName}'
    email = 'scottdminter@gmail.com'
    scope = 'ZohoCRM/crmapi'
    pw = 'uDBsQRjK9epH'
    display_name = 'MANA - 1.0 Python Testing'

    url = url.replace("{Scope}", scope)
    url = url.replace("{UsernameEmailID}", email)
    url = url.replace("{Password}", pw)
    url = url.replace("{ApplicationName}", display_name)

    response = requests.post(url)
    data = response.text
    head = response.headers
    print ('')
    print (url)
    print ('')
    print (response)
    print ('')
    print (data)
    print ('')
    print (head)
    print ('')

main()