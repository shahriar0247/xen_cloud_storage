import os

if not os.path.isdir("files"):
    os.mkdir("files")


global main_dir
main_dir = os.getcwd() + '/files/ftp/'
temp_dir = os.getcwd() + '/files/temp'
delete_dir = os.getcwd() + '/files/deleted/'