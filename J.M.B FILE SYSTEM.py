import os
from pathlib import Path
from shutil import *
import shutil
import sys
from os import system, name
from sys import platform as _platform
from time import sleep 

def searchf():
    os.system('cls')or os.system("cls")
    errors = []                       # The list where we will store results.
    linenum = 0
    print("ENTER DIRECTORY TO SEARCH")
    os.chdir(input())
    print("ENTER NAME TO SEARCH")
    searc=input()
    print("ENTER DOCUMENT NAME")
    DOCN=input()
    substr = searc.lower()          # Substring to search for.
    with open (os.path.abspath(os.path.join(os.getcwd(),'{}.txt'.format(DOCN))), 'rt') as myfile:

        for line in myfile:
            linenum += 1
            if line.lower().find(substr) != -1:    # if case-insensitive match,
                errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
    for err in errors:
        print(err)
    PrintMenu()
#///////////////////////////////////////////////////////// 


#def direct():
#This function move user to his/her path of choice and creates a directory called kombo and creates a file
#called eric.txt where it will list all file

#////////////////////////////////////////////////////////////    
def direct():
    print ("Enter Directory to write TEXT FILE".upper())
    dimov=input()
    print ("Enter directory path containing files".upper())
    diare=input()
    os.chdir(dimov)
    p=Path("kombo")
    if p.exists()and p.is_dir() :
        clear()
        #os.path.join(root,file)
        print ("dir exists".upper())
        d=os.path.abspath(os.path.join(os.getcwd(),"eric.txt"))
        
        PrintMenu()

        print(os.listdir())
        
       
    else:
        k=os.mkdir(p)
        #k=os.mkdir("Educator")
        if p.exists():
            file_path=os.chdir(p)
            #print(file_path)
            
            d=os.path.abspath(os.path.join(os.getcwd(),"eric.txt"))
            with open(d,'w') as f:
                f.write("*"*60)
                f.write("\nHELLO CHAMPION BELOW IS A LIST OF YOUR FILES\n")
                f.write("*"*60)
                f.write("\n")

            count=0    

            for root, subdirs, files in os.walk(diare):
                for file in files:
                    #print(os.path.join(root,file))
                    #print(subdirs)
                    filename,extension = os.path.splitext(file)
                    #print(filename)
                    
                    with open(d,'a') as f:
                        f.write('{}{}'.format(filename,extension))
                        count+=1
                        f.write("\n")
    
            os.system("cls") or os.system("cls")      
            print(count,"FILES WRITTEN TO TEXT FILE AT:",d)
            PrintMenu()



choice = input
def PrintMenu():
    print("\n*******************")
    print("\n Bwana File system".upper())
    print("\n*******************")
    print("  [0]clear screen".upper())
    print("  [1] copy file names".upper())
    print("  [2] Search file content".upper())
    print("  [3] move files".upper())
    print("  [4] copy files".upper())
    print("  [5] Exit".upper())
    choice = input ("Enter a choice: ".upper())
    if choice == '0':
        youros()
    if choice == '1':             
        direct()
        
    elif choice == '2':
        searchf()
    elif choice == '3':
        movfile()
    elif choice == '4':
        copfile()
    elif choice == '5':
        print("\nExiting the system......\n")
        sys.exit(0)

    PrintMenu()

# MOVE FILES MODULE
#THIS MODULE MOVES FILES FROM A DIRECTORY AND ITS SUBDIRECTORY TO ANOTHER OF YOUR CHOICE

def movfile():
    print("="*60)
    print("THIS PROGRAM IS COURTESY OF JOSIAH BWANA\nITS PURPOSE IS TO EASE MOVING FILES IN BULK")
    print("="*60)
    print("\n")
    print("ENTER PATH TO MOVE FILES TO")
    mov_to=input()
    MAIN=mov_to

    print("ENTER PATH TO MOVE FILES FROM")
    DIRS = input()

    for root, subdirs, files in os.walk(DIRS):

        k=0
        for file in files:
            pathto = os.path.join(root,file)
            shutil.move(pathto, MAIN)
            k+=1
    print("="*60)
    print(k,"Files moved successfully")
    print("="*60)
    sleep(5)
    clear()


#THIS MODULE COPIES FILE FROM ROOT DIRECTORY And its subdirectories TO ANOTHER
def copfile():
    print("="*60)
    print("ENTER DIRECTORY TO COPY FILES TO")
    ingia=input()
    cop=Path(ingia)
    print("ENTER DIRECTORY TO COPY FILES FROM")

    ingiza=input()
    print("="*60)
    count=0
    if cop.exists()and cop.is_dir():
    
        for root, subdirs, files in os.walk(ingiza):

            for file in files:
                newf=os.path.join(root,file)
                copy(newf, cop)
                count+=1
    print("*"*60)
    print(count,"Files copied")
    print("*"*60)
    sleep(5)
    clear()


def clear():
    if name== "nt":
        _=system('cls')
    else:
        _=system('clear')
    
    PrintMenu()




    

#CHECK YOUR PLAFROM/OS

def youros():
    if _platform == "linux" or _platform == "linux2":
       # linux
       print (_platform)
       os.system("clear")
       PrintMenu()
    elif _platform == "darwin":
       # MAC OS X
       print (_platform)
       os.system("clear") or os.system("cls")
       PrintMenu()
    elif _platform == "win32":
       # Windows
       print ("your platform is:".upper(),_platform)
       os.system("cls")or os.system("cls")
       PrintMenu()
    elif _platform == "win64":
        # Windows 64-bit
        print (_platform)
        os.system("cls")
        PrintMenu()


if __name__=='__main__':
    youros()



