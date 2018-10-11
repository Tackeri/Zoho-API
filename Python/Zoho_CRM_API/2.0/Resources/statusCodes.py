__author__ = 'MinterS'

### Zoho API 2.0 Status Codes

def statusCode (status):
    if status == 200:
	    message = 'OK	The API request is successful.'
    elif status == 201:	
        message = 'CREATED	Request fulfilled for single record insertion.'
    elif status == 202:	
        message = 'ACCEPTED	Request fulfilled for multiple records insertion.'
    elif status == 204:	
        message = 'NO CONTENT	There is no content available for the request.'
    elif status == 304:	
        message = 'NOT MODIFIED	The requested page has not been modified. In case "If-Modified-Since" header is used for GET APIs'
    elif status == 400:	
        message = 'BAD REQUEST	The request or the authentication considered is invalid.'
    elif status == 401:	
        message = 'AUTHORIZATION ERROR	Invalid API key provided.'
    elif status == 403:	
        message = 'FORBIDDEN	No permission to do the operation.'
    elif status == 404:	
        message = 'NOT FOUND	Invalid request.'
    elif status == 405:	
        message = 'METHOD NOT ALLOWED	The specified method is not allowed.'
    elif status == 413:	
        message = 'REQUEST ENTITY TOO LARGE	The server did not accept the request while uploading a file, since the limited file size has exceeded.'
    elif status == 415:	
        message = 'UNSUPPORTED MEDIA TYPE	The server did not accept the request while uploading a file, since the media/ file type is not supported.'
    elif status == 429:	
        message = 'TOO MANY REQUESTS	Number of API requests per minute/day has exceeded the limit.'
    elif status == 500:	
        message = 'INTERNAL SERVER ERROR	Generic error that is encountered due to an unexpected server error.'
    else:
        message = 'Status Code Not Found'
    return message