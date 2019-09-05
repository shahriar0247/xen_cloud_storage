from flask import Flask, render_template,request
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
    return dirlist, currentdir


app = Flask(__name__)

@app.route('/')
def main():
    dirlist, currentdir = getfolderlist(dirloc)
    return render_template("main.html", dirlist=dirlist, currentdir=currentdir)


@app.route('/path')
def query_example():
    location = request.args.get('location') #if key doesn't exist, returns None
    print("location:                ", location)
    dirlist, currentdir = getfolderlist(location)
    return render_template("main.html", dirlist=dirlist, currentdir=currentdir)
