from app import app
from flask import session, request, render_template,send_from_directory
import os

from app.setting_dir import temp_dir, main_dir, delete_dir 

@app.route('/upload', methods=['POST'])
def uploadfile():
    if request.method == 'POST':
        if request.files:

            _file = request.files['_file']
            
            
            currentfold2 = session['username'] + "/"+ request.form['currentfold2'] 
            currentfold3 = request.form['currentfold2'] 
            print(currentfold2)
            print(currentfold3)
            print("------------------------------------------------")
            if _file.filename in os.listdir(currentfold3):
                error = "File/Folder with the name '" + _file.filename + "' already exists in the server!" 
                return render_template("error.html", error=error, currentdir=currentfold3)
            _file.save(currentfold3+'/' +_file.filename)
            return render_template("upload2.html", url='/path?location=' + currentfold3)
            #return redirect('/path?location=' + currentfold3)
    

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