from pathlib import Path
import os
def readfileandfolder():

    path = Path('')
    items =list( path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items} ")




def Creatingfile():
    readfileandfolder()
    try:
        print("YOUR FILE  IS ON (CREATING MODE)")
        name = input("ENTER THE FILE NAME = ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("WHAT DO YOU WANT TO WRITE IN THIS FILE = ")
                fs.write(data)
            print("FILE  IS CREATED SUCCESSFULLY")
        else :
            print("THIS FILE IS ALREADY CREATED !")
    except Exception as err:
        print(f"AN ERROR IS OUCCURE AS {err}")



def Readingfile():
    readfileandfolder()
    try:
        print("YOUR FILE IS ON (READING MODE)")
        name = input("ENTER THE FILE NAME = ")
        p = Path(name)
        if p.exists() and p.is_file():

            with open(p,"r") as fs:
                data = fs.read()
                print(data)
        else :
            print("THIS FILE NOT EXITS / IS NOT FILE !")
    except Exception as err:
        print(f"AN ERROR IS OUCCURE AS {err}")
    print("FILE IS READED SUCCESSFULLY")


def updatingfile():
    readfileandfolder()
    try:
        print("YOUR FILE IS ON (UPDATING MODE)")
        name = input("ENTER THE FILE NAME = ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("PRESS 1 FOR RENAME A FILE ")
            print("PRESS 2 FOR OVERWRITING  A FILE ")
            print("PRESS 3 FOR APPEND IN A FILE ")

            res = int (input("TELL YOUR RESPONSE = "))
            if res == 1:
                name2 = input("ENTER THE FILE NAME = ")
                p2 = Path(name2)
                p.rename(p2) 
            elif res == 2 :
                with open(p,"w") as fs:
                    data = input("WHAT DO YOU WANT TO WRITE IN FILE = ")
                    fs.write(data)
            elif res == 3:
                with open(p,"w") as fs:
                    data = input("WHAT DO YOU WANT TO APPEND IN FILE = ")
                    fs.write(data)
        else :
            print("THIS FILE NOT EXITS / IS NOT FILE !")
    
    except Exception as err:
            print(f"AN ERROR IS OUCCURE AS {err}")
    print("FILE IS UPDATING SUCCESSFULLY")


def deletingfile():
    readfileandfolder()
    try:
        print("YOUR FILE IS ON (UPDATING MODE)")
        name = input("ENTER THE FILE NAME = ")
        p = Path(name) 
        if p.exists and p.is_file :
            os.remove(p)
        else :
            print("THIS FILE NOT EXITS / IS NOT FILE !")

    except Exception as err :
        print(f"AN ERROR IS OUCCURE AS {err}")

    print("FILE IS DELETED  SUCCESSFULLY")



print("PRESS 1 FOR CREATING A FILE")
print("PRESS 2 FOR READING A FILE")
print("PRESS 3 FOR UPDATING A FILE")
print("PRESS 4 FOR DELETION A FILE")

check = int(input("PLEASE ENTER YOUR RESPONSE = "))

if check == 1 :
    Creatingfile()
elif check == 2 :
    Readingfile()
elif check == 3 :
    updatingfile()
elif check == 4 :
    deletingfile()
else :
    print("PLEASE ENTER VAILD NUMBER !")


