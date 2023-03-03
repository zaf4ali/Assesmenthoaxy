#part 1
#from zipfile import ZipFile

#z=ZipFile("Output.zip",'w')

#z.write("zip.py")
#z.write("renam.py")
#z.write("test.py")
#z.write("test2.py")
#z.write("test123.py")
#z.write("text.txt")
#z.write("text3.txt")


#z.close()


#part2
#import shutil

# define folder path and zip file name
#folder_path = "output"
#zip_file_name = "output_1_0.zip"

# create zip file
#shutil.make_archive(zip_file_name, "zip", folder_path)

# rename the zip file
#import os
#os.rename(zip_file_name + ".zip", zip_file_name)

#part3
#import os

# define folder path
#folder_path = "output"

# get list of all files in folder
#files = os.listdir(folder_path)

# sort files by modification time in ascending order
#files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

# print sorted list of files
#print(files)

#part4

import os

# define folder path
folder_path = "output"

# get list of all files in folder
files = os.listdir(folder_path)

# sort files by modification time in descending order
files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)

# keep only latest 5 files
latest_files = files[:5]

# delete all other files
for file in files[5:]:
    os.remove(os.path.join(folder_path, file))
