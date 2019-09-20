import os
import magic
import base64

dirloc = "/home/dkolate"


def getfolderlist(dirloc):
    try:
        os.chdir(dirloc)
        dirlist = os.listdir()
        dirlist = sorted(dirlist)
        filetype=[]
        filename=[]
        filename1=[]
        for singlefile in dirlist:
            try:
                filetype.append(magic.from_file(singlefile))
            except:
                filetype.append("folder")
            filename.append(singlefile)
        currentdir= os.getcwd()
        currentdir = currentdir.replace('/', 'jf][')
        for a in filename:
            if len(a) > 13:
                a = a[:10] + "....."
            filename1.append(a)
        return filename, filetype, currentdir, filename1
    except:
        return "error", "error","error","error", 

def openasciitext(location):
    filecontents = open(location,"r").readlines()
    return filecontents

def openimage(location):
    with open(location, "rb") as image_file:
        imagecontents = base64.b64encode(image_file.read()).decode("utf-8") 
    return imagecontents


def getcurrentdir(dirloc):
    os.chdir(dirloc)
    currentdir= os.getcwd()
    print("current dir \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n" + currentdir)
    return currentdir


