from app import app
from flask import session, request, render_template,send_from_directory
import os

from app.setting_dir import temp_dir, main_dir, delete_dir 

@app.route('/upload', methods=['POST'])
def uploadfile():
    if request.method == 'POST':
        if request.files:

            _file = request.files['_file']
            
            location = request.form['currentfold2'][1:]
            absolute_location = os.path.join(main_dir, os.path.join(session['username'], location))
            if _file.filename in os.listdir(absolute_location):
                error = "File/Folder with the name '" + _file.filename + "' already exists in the server!" 
                return render_template("error.html", error=error, currentdir=absolute_location)
            _file.save(absolute_location+'/' +_file.filename)
            return render_template("upload2.html", url='/path?location=/' + location)
            #return redirect('/path?location=' + location)
    

@app.route('/download/<path>', methods=['POST'])
def download(path):
    if request.method == 'POST':
        os.chdir(temp_dir)
        os.system('rm -rf *')
        download_dir = request.form['download_dir']
        download_name = request.form['download_name']
        download_dir = main_dir + session['username'] + download_dir + '/'
   

        if os.path.isdir(download_dir + download_name):

            zipfilename = '/' + download_name + '.zip'
	        
    
            zip_file = "'"+temp_dir +zipfilename+"'"

            os.chdir(download_dir)
            download_file =' "' + download_name + '" '
            
            os.system('zip -r ' + zip_file + download_file)
            

            return send_from_directory(temp_dir,download_name + ".zip")
           

        return send_from_directory(download_dir,download_name)