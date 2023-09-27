
from genericpath import isfile
import json
from pathlib import Path
import keyboard
import os

# file i/o class

class dataBase(object):
        def __init__(self, init):
            self.init = init

# construct new filename/check exists
def consFileName(name,chain,what): # who, and what data (tx, balance, etc.)
    newpath = f'~/{name}/{chain}/{what}'
    if not os.path.exists(newpath):
         os.makedirs(newpath)

    filename = str(f'/{name}_{chain}_{what}.json')
    userPath = newpath+filename
    print(userPath)
    my_file = Path(userPath)
    try:
        my_file = my_file.resolve(strict=True)

    except FileNotFoundError:
            print("File not found... Creating file...")
            my_file = open(userPath, 'x')
            my_file.close()
            return userPath
    else:
        print('File exists!')
        return userPath

# scrub file from database 
def deleteFile(userPath):

    # delete file

    my_file = Path(userPath)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("Already deleted!")
    else:
        os.remove(userPath)
        print("File deleted!")
        print ("\nPress Enter to continue...")
        keyboard.wait('enter')

        return 

# read from data base
def readFrom(userPath):

    my_file = Path(userPath)
    try:
        my_file = my_file.resolve(strict=True)
    except FileNotFoundError:
         print("File not found...")
         
    else:
        try:
            with open(userPath,'r') as my_file: 
                data = json.load(my_file)
                my_file.close()
                return data
        except json.decoder.JSONDecodeError:
            print("No data on file...\n")
            print("Running API call to populate database...")
            print("\nPress Enter to continue...")
            keyboard.wait('enter')



# write data to file
def writeTo(userPath, data): # this should dynamically alter, append, remove data

    my_file = Path(userPath)
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

        with open(userPath,'w') as out_file:
            # update file 
            json.dump(data, out_file, indent=6)
            out_file.truncate()
            out_file.close()

    return 


# combine chains to return overall portfolio
def combineChains(name, what, chains):

    direct = f'~/{name}/{what}/'
    _,_, files = next(os.walk(direct))
    file_count = len(files)

    data = []
    for i in range(file_count):
         with open(f'~/{name}/{what}/{chains[i]}/{name}_{what}_{chains[i]}.json','r') as out_file:
             data[i] = json.load(out_file)
    print(data)
    return



