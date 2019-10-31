import os
import magic
import base64

dirloc = "/home/dkolate/Desktop"


def getfolderlist(dirloc):
    try:
        os.chdir(dirloc)
        dirlist = os.listdir()
        dirlist = sorted(dirlist)
        filetype = []
        filename = []
        filename1 = []
        filename2 = []
        filetype1 = []
        for singlefile in dirlist:
            try:
                filetype.append(magic.from_file(singlefile))
            except:
                filetype.append("folder")
            filename.append(singlefile)
        currentdir = os.getcwd()
        currentdir = currentdir.replace('/', 'jf][')
        for a in filename:
            if len(a) > 22:
                a = a[:19] + "..."
            filename1.append(a)


        for b in filename:
            if len(b) > 14:
                b = b[:11] + "..."
            filename2.append(b)


        for c in filetype:
            if len(c) > 20:
                c = c[:17] + '...'
            filetype1.append(c)

        return filename, filetype, currentdir, filename1, filename2, filetype1
    except:
        return "error", "error","error","error","error", "error" 

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
    return currentdir


