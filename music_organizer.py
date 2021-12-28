import os

# check current working directory
# print(os.getcwd())

# change directory to specific destination
os.chdir("C:\Music")

# check what inside directory
for file in os.listdir():
    # split file extension from file name
    file_name, file_ext = os.path.splitext(file)
    f_title, f_volume, f_number = file_name.split('-')
    # strip white spaces
    f_title = f_title.strip()
    f_volume= f_volume.strip()
    # remove hash sign from number and make that two digits number
    f_number= f_number.strip()[1:].zfill(2)
    new_name = f'{f_number}-{f_volume}-{f_title}{file_ext}'

    # change files names
    os.rename(file, new_name)