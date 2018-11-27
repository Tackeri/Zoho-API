__author__ = 'MinterS'

### Zoho Books API V3.0 Status Codes

def statusCode (status):
    if status == 200:
	    message = 'Success - The request was successfully completed.'
    elif status == 201:	
        message = 'Created - The request was a success and one or more resources have been created.'
    elif status == 400:	
        message = 'Bad request - The request cannot be performed. Usually because of malformed parameter or missing parameter.'
    elif status == 401:	
        message = 'Unauthorized (Invalid AuthToken) - Request was rejected because of invalid AuthToken.'
    elif status == 403:	
        message = 'Forbidden - The user does not have enough permission or possibly not an user of the respective organization to access the resource.'
    elif status == 404:	
        message = 'URL Not Found - The URL you’ve sent is wrong. It’s possible that the resource you’ve requested has been moved to another URL.'
    elif status == 405:	
        message = 'Method Not Allowed - The requested resource does not support the HTTP method used. For example, requesting List of all customers API with PUT as the HTTP method.'
    elif status == 406:	
        message = 'Not Acceptable - The requested response type is not supported by the client.'
    elif status == 429:	
        message = 'Too many requests - Too many requests within a certain time frame. To know more about api call limits, click here.'
    elif status == 500:	
        message = 'Server error - Zoho Books server encountered an error which prevents it from fulfilling the request. Although this rarely happens, we recommend you to contact us at support@zohobooks.com if you receive this error.'
    else:
        message = 'Status Code Not Found'
    return message