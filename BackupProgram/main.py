# import os
# import shutil

# source = input("Please Enter The Location of the directory\n")
# destination = input("\nPlease Enter The Destination of the directory\n\n")

# try:
#     dest = shutil.copy(source, destination)
#     print("\nFile Backup")

# except PermissionError:
#     print("\nPlease check the Path of the file")

# except FileNotFoundError:
#     print("\nPlease Check the file Name")


# D:\Backup



import os
import shutil

# os.mkdir("D:/Apps/Python/BackupProgram/file.md")
# os.makedirs("D:/Apps/Python/BackupProgram/txt/dir1")
# os.getcwd()

# isExit = os.path.exists("d:/Apps/Python/BackupProgram/main.py")
# print(isExit)

path = "D:\Apps\Python\BackupProgram"
root = os.path.splitext(path)
print("Path: ",root[0],"  ","Ext: ", root[1])

os.listdir(path)

input()