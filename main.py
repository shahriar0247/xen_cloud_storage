from flask import Flask, redirect, render_template, request, session, abort
import os
import magic
import webbrowser


dirloc = "/home/dkolate"


def getfolderlist(dirloc):
    os.chdir(dirloc)
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
    currentdir= os.getcwd()
    currentdir = currentdir.replace('/', 'jf..>')
    
    return filename, filetype, currentdir

def openasciitext(location):
    filecontents = open(location,"r").readlines()
    return filecontents

app = Flask(__name__)



app.secret_key = os.urandom(12)
    


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename, filetype, currentdir = getfolderlist(dirloc)
        number_of_files = len(filename)
        return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files)


@app.route('/login', methods=['POST'])
def do_admin_login():
    if session.get('logged_in'):
        return home()
    else:
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True

        else:
            return 'Wrong password'
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/path')
def query_example():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        location = request.args.get('location')
        location = location.replace("jf..>", "/")
        print(location)
        if os.path.isdir(location):
            filename, filetype, currentdir = getfolderlist(location)
            number_of_files = len(filename)
            return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files)
        elif os.path.isfile(location):
            filecontents = openasciitext(location)
            return render_template('file.html', filecontents=filecontents)
       