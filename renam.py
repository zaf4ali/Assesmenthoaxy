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