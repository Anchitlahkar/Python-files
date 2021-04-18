import os
import shutil

# os.mkdir("D:/Apps/Python/BackupProgram/file.md")
# os.makedirs("D:/Apps/Python/BackupProgram/txt/dir1")
# os.getcwd()

# isExit = os.path.exists("d:/Apps/Python/BackupProgram/main.py")
# print(isExit)

# path = "d:\Apps\Python\BackupProgram\main.py"
# root = os.path.splitext(path)
# print("Path: ",root[0],"  ","Ext: ", root[1])

# os.listdir(path)

source = "D:/Code/Uninitillize git command.txt"
destination = "D:/FileHistory"

dest= shutil.move(source, destination)



import os
import shutil

# source = input("Please Enter The Location of the directory\n\n")
# destination = input("Please Enter The Destination of the directory\n\n")

# dest = shutil.copy(source, destination)

try:
    source = "D:/TEXT/md/text3.md"
    destination = "D:/Backup"

    dest= shutil.copy(source, destination)
    print("File Backup")

except PermissionError:
    print("PermissionError...")

