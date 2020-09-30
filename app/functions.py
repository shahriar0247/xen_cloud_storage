import os
import magic
import base64

dirloc = os.getcwd() + "/files/ftp"
dirloc2= dirloc

def getfolderlist(dirloc, username):
    
    if username not in dirloc and "/" + username not in dirloc:
        dirloc = os.path.join(dirloc2,username)+ dirloc
    else: dirloc = dirloc2 + dirloc

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
        
        for a in filename:
            if len(a) > 22:
                a = a[:17] + "..."
            filename1.append(a)


        for b in filename:
            if len(b) > 14:
                b = b[:9] + "..."
            filename2.append(b)


        for c in filetype:
            if len(c) > 20:
                c = c[:15] + '...'
            filetype1.append(c)
        currentfold2 = currentdir.replace(os.getcwd() + "/files/ftp/" + username.replace("/",""), '')
       
        return filename, filetype, currentdir, filename1, filename2, filetype1, currentfold2
    except:
        return "error", "error","error","error","error", "error" 

def openasciitext(location):
    filecontents = open(location,"r").readlines()
    return filecontents

def openimage(location):
    with open(location, "rb") as image_file:
        imagecontents = base64.b64encode(image_file.read()).decode("utf-8") 
    return imagecontents


def getcurrentdir(dirloc, username):
    dirloc = dirloc2 + dirloc + username
 
    os.chdir(dirloc)
    currentdir= os.getcwd()
    return currentdir


