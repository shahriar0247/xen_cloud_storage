
from app import app
from flask import session, render_template, request, redirect
from app import process_files
import os
import magic

@app.route('/')
def home():
    if 'username' not in session:
        return render_template('login.html')
    else:
        return main()



@app.route('/path', methods=['GET', 'POST'])
def main():
    
    if 'username' not in session:
        return render_template('login.html')
    else:
        
        if request.method == 'POST':
            if request.files:
                location = request.args.get('location')
                
                currentdir = process_files.getcurrentdir(process_files.dirloc+location, session['username'])
                _file = request.files['_file']
                _file.save(os.path.join(currentdir, _file.filename))

            return redirect(request.url)
        elif request.method == "GET":
            if request.args.get('location') == None:
                location = ''
            else:
                location = request.args.get('location')
            
            path = os.path.join(process_files.dirloc, os.path.join(session['username'],location[1:]))
        
         
            if os.path.isdir(path):
                
                filename, filetype, currentdir, filename1, filename2, filetype1, currentfold2, filesize = process_files.getfolderlist(location, session['username'])
                filename21, filetype2, currentdir2, filename12, filename22, filetype12, currentfold22, filesize = process_files.getfolderlist("/", session['username'])

                if filename == "error":
                    return render_template("error.html")
                else:
                    number_of_files = len(filename)
                    number_of_files2 = len(filename21)
                    
                    return render_template("main.html", filename=filename, filetype=filetype, currentdir=currentdir, filename1=filename1, filename2=filename2, filetype1=filetype1, currentfold2=currentfold2, number_of_files=number_of_files, filename21=filename21, filetype2=filetype2, currentdir2=currentdir2, filename12=filename12, filename22=filename22, filetype12=filetype12, currentfold22=currentfold22, number_of_files2=number_of_files2, filesize=filesize)
            elif 'ASCII' in magic.from_file(path):
                filecontents = process_files.openasciitext(path)
                return render_template('file.html', filecontents=filecontents)
            elif 'image' in magic.from_file(path):
                imagecontents = process_files.openimage(path)
                return render_template('image.html', imagecontents=imagecontents)

            else:
                return 'Unknown error'

