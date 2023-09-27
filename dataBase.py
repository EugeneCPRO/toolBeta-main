
import json
from pathlib import Path
import keyboard
import os
import pandas


# file i/o class

class dataBase(object):
        def __init__(self, init):
            self.init = init

# construct new filename/check exists
def consFileName(name, what,chain): # who, and what data (tx, balance, etc.)
    filename = str(f'{name}_{chain}_{what}.json')
    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)

    except FileNotFoundError:
            print("File not found... Creating file...")
            my_file = open(filename, 'x')
            my_file.close()
            return filename
    else:
        print('File exists!')
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
        os.remove(filename)
        print("File deleted!")
        print ("\nPress Enter to continue...")
        keyboard.wait('enter')

        return 

# read from data base
def readFrom(filename):

    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("File not found...")
         
    else:
        try:
            with open(filename)as file: 
                data = file.read()
                data = json.loads(data)
        except json.decoder.JSONDecodeError:
            print("No data on file...\n")
            print("Running API call to populate database...")
            print ("\nPress Enter to continue...")
            keyboard.wait('enter')

        return data




# write data to file
def writeTo(filename, data): # this should dynamically alter, append, remove data

    my_file = Path(filename)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("File not found...")

    # else:
    #     try:
    #         oldData = readFrom(filename)
    #     except json.decoder.JSONDecodeError:
    #          out_file = open(filename,"w")
    #          json.dump(data,out_file, indent=6)
    #          out_file.close()

    else:
    # alter data (example, will be if statements)

        with open(filename,'w') as out_file:
            newData = json.dumps(data)
            # update file 
            json.dump(newData, out_file, indent=6)
            out_file.close()

    return 


