__author__ = 'MinterS'

import os



# Token Files
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
grantTokenFile = os.path.join(THIS_FOLDER, 'grant_token.txt')
accessTokenFile = os.path.join(THIS_FOLDER, 'access_token.txt')
refreshTokenFile = os.path.join(THIS_FOLDER, 'refresh_token.txt')
# grantTokenFile = '2.0/Authentication/grant_token.txt'
# accessTokenFile = '2.0/Authentication/access_token.txt'
# refreshTokenFile = '2.0/Authentication/refresh_token.txt'

# Save access token to file 
def saveAccess (token):
    edit_file = open(accessTokenFile, 'w')
    edit_file.write(token)
    edit_file.close()

# Save refresh token to file
def saveRefresh (token):
    edit_file = open(refreshTokenFile, 'w')
    edit_file.write(token)
    edit_file.close()

# Get grant token from file
def getGrantToken ():
    f = open(grantTokenFile, 'r')
    grantToken = f.readline()
    f.close()
    return grantToken

# Get access token from file
def getAccess ():
    f = open(accessTokenFile, 'r')
    token = f.readline()
    f.close()
    accessToken = 'Zoho-oauthtoken ' + token
    return accessToken

# Get refresh token from file
def getRefresh ():
    f = open(refreshTokenFile, 'r')
    token = f.readline()
    f.close()
    refreshToken = token
    return refreshToken