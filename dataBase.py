
import json
from pathlib import Path
import pydoc

# file i/o class

class dataBase(object):
        def __init__(self, init):
            self.init = init

# construct new filename
def consFileName(name, datatype): # who, and what data (tx, balance, etc.)
     
     filename = str(f'{name}_{datatype}.txt')
     return filename


# scrub file from database 
def deleteFile(filename):

    # delete file

    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("Already deleted!")
    else:
        # delete file
        # has it been deleted?
        # print success/error

        return 

# read from data base
def readFrom(filename):

    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("File not found...")
         
    else:
        with open(filename)as file: 
            data = file.read()
            data = json.loads(data)
        return data




# write data to file
def writeTo(filename, data): # this should dynamically alter, append, remove data (dict)

    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("File not found...")
    else:
        prevFile = readFrom(filename)

        # alter data (example, will be if statements)
        upFile = prevFile.append(data) # other functions will be implemented as required

        # update file 
        json.dump(upFile, filename)

    return 


