from flask import Flask, render_template,request, request
import os



dirloc = "/home/dkolate"


def getfolderlist(dirloc):
    dirloc = dirloc.replace("jf..>", "/")
    print(dirloc)
    os.chdir(dirloc)
    currentdir= os.getcwd()
    currentdir = currentdir.replace('/', 'jf..>')
    print("changed to home")
    dirlist = os.listdir()
    dirlist = sorted(dirlist)
    filetype=[]
    filename=[]
    for singlefile in dirlist:
        try:
            filetype.append(magic.from_file(singlefile))
        except:
            filetype.append("folder")
        filename.append(singlefile)
    return filename, filetype, currentdir


app = Flask(__name__)




@app.route('/')
def main():
    filename, filetype, currentdir = getfolderlist(dirloc)
    return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir)

@app.route('/path')
def query_example():
    location = request.args.get('location') #if key doesn't exist, returns None
    print("location:                ", location)
    filename, filetype, currentdir = getfolderlist(location)
    return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir)

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    return render_template("login.html")