from app import app
from app import database
from flask import request, url_for, redirect, session, render_template
import bcrypt
import os
from app.setting_dir import main_dir

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        login_user = database.users.find_one({'users': request.form['username']})
        
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
            
                return redirect(url_for('main'))
            return 'Invalid Password <a href="/login">Try again</a>'
     
        return 'User does not exists do you want to <a href="/signup">signup</a>'

    elif request.method == 'GET':
        return render_template('/login/login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = database.users.find_one({'users':request.form['username']})
        if existing_user == None:
            if len(request.form['password']) < 63 and len(request.form['password']) > 7:
                hashedpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
           
                database.users.insert_one({'users':request.form['username'], 'password': hashedpass})
                database.storage.insert_one({'users':request.form['username'], "stored_size": 0})
                os.mkdir(os.path.join(main_dir, request.form['username']))
                return redirect(url_for('login'))
            return 'Please use a password more then 8 characters and less then 63 characters. <a href="/signup">Try again.<a>'
        return 'User exists. <a href="/login">Login?<a>'

    elif request.method == 'GET':
        
        return render_template('/login/signup.html')
