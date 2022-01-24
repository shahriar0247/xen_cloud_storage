from app import app, database
from flask import flash, redirect, session, request, render_template,send_from_directory
import os
import settings

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
            real_file_location = absolute_location+'/' +_file.filename
            _file.save(real_file_location)
            size = os.stat(real_file_location).st_size
            storage_after_upload = database.storage.find_one({'users':session['username']})["stored_size"] + size
            print(storage_after_upload)
            if (storage_after_upload) > settings.USER.max_storage:
                os.remove(real_file_location)
                flash('You are exceeding storage size limit, file is not uploaded', "error")
            else:
                pass
                database.storage.update_one({'users':session['username']},{ "$set": {"stored_size": storage_after_upload}})
            return redirect('/path?location=/' + location)
    

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