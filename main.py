from flask import Flask, redirect, render_template, request, session, abort, send_from_directory
import webbrowser
from functions import *



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
            return request.form['password']
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/path', methods=['GET','POST'])
def main():
    if not session.get('logged_in'):
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
                location = '/home/dkolate'
            
            if os.path.isdir(location):
                filename, filetype, currentdir, filename1 = getfolderlist(location)
                if filename == "error":
                    return render_template("error.html")
                else:
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

@app.route('/upload', methods=['GET','POST'])
def uploadfile():
    if request.method == 'POST':
        if request.files:
           
            _file = request.files['_file']
    
            _currentdir = request.form['currentdir']
        
            _file.save(os.path.join(_currentdir, _file.filename))

            return redirect(request.url)
    return main()

@app.route('/download')
def ol():
    return send_from_directory(directory='templates', filename='file.zip')

@app.route('/lol')
def lol():
    return send_from_directory(directory='templates', filename='file.zip')




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4100, debug=True)