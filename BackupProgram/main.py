import os
import shutil

source = input("Please Enter The Location of the directory\n")
destination = input("\nPlease Enter The Destination of the directory\n\n")

try:
    dest = shutil.copy(source, destination)
    print("\nFile Backup")

except PermissionError:
    print("\nPlease check the Path of the file")

except FileNotFoundError:
    print("\nPlease Check the file Name")


# D:\Backup