from flask import Flask, redirect, render_template, request, session, abort, send_from_directory, url_for
import webbrowser
from functions import *
import zipfile
import pymongo
import bcrypt
import datetime


app = Flask(__name__)

app.secret_key = os.urandom(12)

db = pymongo.MongoClient().xenusersdb
users = db.users
@app.route('/')
def home():
    if 'username' not in session:
        return render_template('login.html')
    else:
        return main()
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        login_user = users.find_one({'users': request.form['username']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('main'))
            return 'Invalid Password <a href="/login">Try again</a>'
        return 'User does not exists do you want to <a href="/register">Register</a>'

    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'users':request.form['username']})
        if existing_user == None:
            
            hashedpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())

            users.insert_one({'users':request.form['username'], 'password': hashedpass})
            return redirect(url_for('login'))
        return 'user exists'

    elif request.method == 'GET':
        
        return render_template('register.html')


@app.route('/path', methods=['GET', 'POST'])
def main():
    if 'username' not in session:
        return render_template('login.html')
    else:
        if request.method == 'POST':
            if request.files:
                location = request.args.get('location')
                location = location.replace("jf][", "/")
                currentdir = getcurrentdir(location)
                _file = request.files['_file']
                _file.save(os.path.join(currentdir, _file.filename))

            return redirect(request.url)
        elif request.method == "GET":
            try:
                location = request.args.get('location')
                location = location.replace("jf][", "/")
            except:
                location = '/home/dkolate/Desktop'

            if os.path.isdir(location):
                filename, filetype, currentdir, filename1, filename2, filetype1 = getfolderlist(
                    location)
                if filename == "error":
                    return render_template("error.html")
                else:
                    number_of_files = len(filename)
                    return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files, filename1=filename1, filename2=filename2, filetype1=filetype1)
            elif 'ASCII' in magic.from_file(location):
                filecontents = openasciitext(location)
                return render_template('file.html', filecontents=filecontents)
            elif 'image' in magic.from_file(location):
                imagecontents = openimage(location)
                return render_template('image.html', imagecontents=imagecontents)

            else:
                return 'Unknown error'


@app.route('/upload', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        if request.files:

            _file = request.files['_file']

            _currentdir = request.form['currentdir']

            _file.save(os.path.join(_currentdir, _file.filename))

            return redirect(request.url)
    return main()


@app.route('/download/<path>', methods=['POST', 'GET'])
def download(path):
    if request.method == 'POST':
        filename = request.form['download-name']
        dirloca = request.form['download-dir']
        location = dirloca + '/' + filename
        if os.path.isdir(location):
            zipfilename = location + '.zip'
            os.system('zip -r ' + zipfilename + " " + location)
            filename = filename + '.zip'
       
        return send_from_directory(directory=dirloca, filename=filename)

    else: return 'error'


@app.route('/htmltopython', methods=['POST', 'GET'])
def htmltopython():
    if request.method == 'POST':
        action = request.form['htmltopython']
        currentdir = request.form['currentdir1']
        menu1text2 = request.form['menu1text2']
        if action == 'new-folder':
            menu1text2 = menu1text2.replace(" ","\ ")
            menu1text2 = menu1text2.replace(";"," ")
            menu1text2 = menu1text2.replace(">"," ")

            os.system('mkdir ' + currentdir + '/' + menu1text2)
            return main()
        elif action.startswith('delete'):
            action = action.split('%20,,@#')
            os.system('mv ' + action[1] + ' /home/dkolate/deleted/' + action[1] + '\ ' + str(datetime.datetime.now()).replace(' ', ''))
            return main()
        else:
            return 'error1'
    else:
        return main()
    


if __name__ == "__main__":
    app.run(host='3.1.5.100', port=4200, debug=True)
