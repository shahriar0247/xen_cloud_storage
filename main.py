from flask import Flask, redirect, render_template, request, session, abort
import os
import magic
import webbrowser
import base64

dirloc = "/home/dkolate"


def getfolderlist(dirloc):
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
    currentdir = currentdir.replace('/', 'jf..>')
    for a in filename:
        if len(a) > 13:
            a = a[:10] + "..."
            print(a)
        filename1.append(a)
    return filename, filetype, currentdir, filename1

def openasciitext(location):
    filecontents = open(location,"r").readlines()
    return filecontents

def openimage(location):
    with open(location, "rb") as image_file:
        imagecontents = base64.b64encode(image_file.read()).decode("utf-8") 
    return imagecontents

app = Flask(__name__)



app.secret_key = os.urandom(12)
    


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename, filetype, currentdir, filename1 = getfolderlist(dirloc)
        number_of_files = len(filename)
        return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files, filename1=filename1)


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
            filename, filetype, currentdir, filename1 = getfolderlist(location)
            number_of_files = len(filename)
            return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files, filename1=filename1)
        elif 'ASCII' in magic.from_file(location):
            filecontents = openasciitext(location)
            return render_template('file.html', filecontents=filecontents)
        elif 'image' in magic.from_file(location):
            imagecontents = openimage(location)
            return render_template('image.html', imagecontents=imagecontents)

        else:
            return 'Unknown error'
       