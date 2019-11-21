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
awaiting_users = db.awaitingusers

main_dir = '/home/dkolate/Desktop/all/ftp/ftp'
temp_dir = '/home/dkolate/Desktop/all/ftp/temp'
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
        print(login_user['users'])
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
            
                return redirect(url_for('main'))
            return 'Invalid Password <a href="/login">Try again</a>'
        elif awaiting_users.find_one({'users': request.form['username']}):
            return 'Awaiting for manual authentication'
        return 'User does not exists do you want to <a href="/register">Register</a>'

    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'users':request.form['username']})
        if existing_user == None:
            if len(request.form['password']) < 63 and len(request.form['password']) > 8:
                hashedpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
                print(len(request.form['password']))
                awaiting_users.insert_one({'users':request.form['username'], 'password': hashedpass})
                return redirect(url_for('login'))
            return 'Please use a password more then 8 characters and less then 63 characters. <a href="/register">Try again.<a>'
        return 'User exists. <a href="/login">Login?<a>'

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
                
                currentdir = getcurrentdir(dirloc + location)
                _file = request.files['_file']
                _file.save(os.path.join(currentdir, _file.filename))

            return redirect(request.url)
        elif request.method == "GET":
            if request.args.get('location') == None:
                location = ''
            else:
                location = request.args.get('location')

            if os.path.isdir(dirloc + location):
                
                filename, filetype, currentdir, filename1, filename2, filetype1, currentfold2 = getfolderlist(
                    location)
            
                if filename == "error":
                    return render_template("error.html")
                else:
                    number_of_files = len(filename)
                    return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, number_of_files=number_of_files, filename1=filename1, filename2=filename2, filetype1=filetype1, currentfold2=currentfold2)
            elif 'ASCII' in magic.from_file(dirloc + location):
                filecontents = openasciitext(dirloc + location)
                return render_template('file.html', filecontents=filecontents)
            elif 'image' in magic.from_file(dirloc + location):
                imagecontents = openimage(dirloc + location)
                return render_template('image.html', imagecontents=imagecontents)

            else:
                return 'Unknown error'


@app.route('/upload', methods=['POST'])
def uploadfile():
    if request.method == 'POST':
        if request.files:

            _file = request.files['_file']
            
            
            currentfold2 = request.form['currentfold2']
            
            _file.save(main_dir + currentfold2+'/' +_file.filename)
          
            return redirect('/path?location=' + currentfold2)
    

@app.route('/download/<path>', methods=['POST'])
def download(path):
    if request.method == 'POST':
        download_dir = request.form['download_dir']
        download_name = request.form['download_name']
        download_dir = main_dir + download_dir + '/'
        print(download_dir + download_name)


        if os.path.isdir(download_dir + download_name):

            zipfilename = '/' + download_name + '.zip'
            os.system('zip -r ' + temp_dir + zipfilename + ' ' + download_dir + download_name)
            return send_from_directory(temp_dir,zipfilename)
           

        return send_from_directory(download_dir,download_name)


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

            os.system('mkdir ' +main_dir+ currentdir + '/' + menu1text2)
            return redirect('/path?location=' + currentdir)
        elif action.startswith('delete'):
            action = action.split('%20,,@#')
            os.system('mv ' + main_dir +currentdir + '/'  + action[1] + ' /home/dkolate/Desktop/all/ftp/deleted/' + action[1] + '\ ' + str(datetime.datetime.now()).replace(' ', ''))
            
            return redirect('/path?location=' + currentdir)
        else:
            return 'error1'
        
    else:
        return redirect(url_for('main'))
    


if __name__ == "__main__":
    app.run(host='3.1.5.101', port=4200, debug=True)
