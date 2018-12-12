from .http import Http
import json

class Users:
    def checkUsernameExists(uname):
        a = Http.getRequest("https://www.roblox.com/UserCheck/DoesUsernameExist?username="+str(uname))
        b = a.decode("utf-8")
        c = json.loads(b)
        if c['success'] == True:
            return True
        else:
            return False



