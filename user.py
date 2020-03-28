import json
import hashlib

def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def readFile(path):
    with open(path) as f:
        return f.read()

def writeData(data):
    with open('./users.json', 'w') as f:
        f.write(
            json.dumps(
                data, 
                sort_keys=True, 
                indent=4, 
                separators=(',', ': '))
        )

def isInTheJson(theUserName):
    for i in jsonOfUsers:
        if i['userName'] == theUserName:
            return True
    return False

def dataToUserObjAndAdd(userName, password):
    _data = User(userName, password)
    userObj.append(_data)
    return _data

def allThedataToUserObj():
    userObj = []
    for i in jsonOfUsers:
        dataToUserObjAndAdd(i['userName'], i['password'])

class User:
    def __init__(self, userName, password):
        self.books = []
        self.userName = userName
        self.password = password

    def doSomeStupidThings(self):
        print('User Name: {} Password: {}'.format(self.userName, self.password))

jsonOfUsers = json.loads(readFile('./users.json'))
userObj = []
allThedataToUserObj()


def newUser(userName, password):
        userName = userName
        password = sha256(password)
        jsonOfUsers.append({
            'userName': userName,
            'password': password
        })
        writeData(jsonOfUsers)
        allThedataToUserObj()

