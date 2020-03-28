import json

def readFile(path):
    with open(path) as f:
        return f.read()


def writeData(data):
    with open('./books.json', 'w') as f:
        f.write(
            json.dumps(
                data, 
                sort_keys=True, 
                indent=4, 
                separators=(',', ': '))
        )

jsonOfBooks = json.loads(readFile('./books.json'))

class Book:
    def __init__(self, name, isBorrowed=False):
        self.name = name
        self.isBorrowed = isBorrowed