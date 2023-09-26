
import json
# file i/o class

class dataBase(object):
        def __init__(self, init):
            self.init = init

# construct new filename
def consFileName(name, datatype): # who, and what data (tx, balance, etc.)
     
     filename = str(f'{name}_{datatype}.txt')
     return filename


# check if a file already exists
def checkExist(filename): # files are assigned on a per name basis (see main)

    return # boolean true/false

# scrub file from database 
def deleteFile(filename):

    # delete file

    valid = checkExist(filename)

    # has it been deleted
    # print success/error

    return 

# read from data base
def readFrom(filename):

    with open(filename)as file: # replace sample doc with "filename"
        data = file.read()
        data = json.loads(data)

    return data

# write data to file
def writeTo(filename, data): # this should dynamically alter, append, remove data (dict)
            
    prevFile = readFrom(filename) # open file

    # alter data (example, will be if statements)
    upFile = prevFile.append(data) # other functions will be implemented as required

    # update file 
    json.dump(upFile, filename)

    # alter data

    return 


