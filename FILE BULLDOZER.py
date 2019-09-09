import os
import shutil
#MAIN = r'\\wsetbn-semantex\Orange_Pride\Logs\REL19_09_Execution_Videos\v-jobwan'
#MAIN = r'C:\Users\\Bwana\Desktop\kombo'
#MAIN=r'\\wsetbn-semantex\Orange_Pride\SEManTEX\Tools'
print("="*60)
print("THIS PROGRAM IS COURTESY OF JOSIAH BWANA\nITS PURPOSE IS TO EASE MOVING FILES IN BULK")
print("="*60)
print("\n")
print("ENTER PATH TO MOVE FILES TO")
mov_to=input()
MAIN=mov_to
#MAIN = r'C:\Users\\Bwana\Desktop\New'
#DIRS = r'C:\Users\Bwana\Desktop\New folder'
#DIRS = r'C:\Users\Bwana\Desktop\.netv4'
print("ENTER PATH TO MOVE FILES FROM")
DIRS = input()
#DIRS = r'\\wsetbn-semantex\Orange_Pride\Logs\REL19_09_Execution_Videos\v-jobwan'
for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('root', subdirs)
    print('root', files)
    k=0
    for file in files:
        path = os.path.join(root,file)
        shutil.move(path, MAIN)
        k+=1
print("="*60)
print(k,"Files moved successfully")
print("="*60)
