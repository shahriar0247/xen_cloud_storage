from flask import Flask, redirect, render_template, request, session, abort
import webbrowser
from functions import *



app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000, debug=True)
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

@app.route('/path')
def query_example():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        location = request.args.get('location')
        location = location.replace("jf][", "/")
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
       