from app import app
from flask import request, session, render_template, redirect, url_for
import os
from app.setting_dir import temp_dir, main_dir, delete_dir 
import datetime

@app.route('/htmltopython', methods=['POST'])
def htmltopython():
    if request.method == 'POST':
        action = request.form['htmltopython']
        currentdir2 = request.form['currentdir1'][1:]
        currentdir = os.path.join(session['username'], currentdir2 )
        
       
        menu1text2 = request.form['menu1text2']
        if action == 'new-folder':
            menu1text2 = menu1text2.replace(" ","\\ ")
            menu1text2 = menu1text2.replace(";"," ")
            menu1text2 = menu1text2.replace(">"," ")
            location = os.path.join(main_dir,currentdir)
            print(main_dir + location)
            if menu1text2 in os.listdir(location):
                
                error = "Folder with the name '" + menu1text2 + "' already exists!"
                return render_template("error.html", error=error, currentdir=currentdir2)
            else: 
                os.system('mkdir "' +main_dir+ currentdir + '/' + menu1text2 + '"')
           
            
            return redirect('/path?location=/' + currentdir2)
        elif action.startswith('delete'):
            action = action.split('%20,,@#')
            os.system('mv "' + main_dir +currentdir + '/'  + action[1] + '" "' + delete_dir + action[1] + ' ' + str(datetime.datetime.now()).replace(' ', '') + '"')
            return redirect('/path?location=/' + currentdir2)
        else:
            return 'error1'
        
    else:
        return redirect(url_for('main'))
    
