import requests
import json

class Http:
    Token = None
    Cookie = None
    # GET
    # Parameters: url - target URL
    def getRequest(url):
        payload = requests.get(str(url))
        statuscode = payload.status_code
        content = payload.content
        if statuscode is not 200:
            return print("Error while requesting: " + json.dumps(payload))
        return content

    # GET
    # Parameters: url - target URL, payload = JSON key-value pairs
    def postRequest(url, params):
        headers = {'Content-Type': 'application/json'}
        print(params)
        payload = requests.post(str(url), data=params, headers=headers)
        statuscode = payload.status_code
        content = payload.content
        if int(statuscode) == 200:
            return payload.json()
        elif int(statuscode) == 403:
            headers = {'Content-Type': 'application/json', 'X-CSRF-TOKEN': payload.headers['X-CSRF-TOKEN']}
            payload = requests.post(str(url), data=params, headers=headers)
            statuscode = payload.status_code
            if Http.Cookie == None:
               Http.Cookie = str(payload.headers['Set-Cookie'])[15:700]
            if int(statuscode) != 200:
                return statuscode
            return payload.json()
        else:
            return payload.json()
