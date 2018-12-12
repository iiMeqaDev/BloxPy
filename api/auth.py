from .http import Http
import requests
import json

class Auth:
    def AuthorizeUsername(Username, Password):
        jsondata = {}
        jsondata['ctype'] = "Username"
        jsondata['cvalue'] = Username
        jsondata['password'] = Password
        a = Http.postRequest('https://auth.roblox.com/v2/login', json.dumps(jsondata))
        return a