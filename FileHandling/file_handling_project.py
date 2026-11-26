from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.iterdir())
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of your file :- ")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("Enter the content you want to add in the file :- ")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exist")
    except Exception as err:
        print(f"An error occured as {err}")
        
def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Successfully read data")
        else:
            print("The file does not exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = print("Enter the name of the file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")
                
            res = int(input("Enter your response :- "))
                
            if res == 1:
                name2 = input("Enter the name you want to update ")
                p2 = Path(name2)
                p.rename(p2)
                    
            if res == 2:
                with open(p,'w') as fs:
                    data = input("Tell what you want to write in file, this will overwrite the data : ")
                    fs.write(data)
                        
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Tell what you want to append in file : ")
                    fs.write(data)
    except Exception as e:
        print(f"An error occured as {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of your file :- ")
        p = Path(name)
        
        if p.exists() and p.is_file():
            os.remove(name)
            print("File Removed Successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occurred as {err}")

print("Enter 1 to create a file")
print("Enter 2 to read a file")
print("Enter 3 to update a file")
print("Enter 4 to delete a file")

check = int(input("Enter your response = "))

if  check == 1:
    createfile()
    
if check == 2:
    readfile()
    
if check == 3:
    updatefile()
    
if check == 4:
    deletefile()