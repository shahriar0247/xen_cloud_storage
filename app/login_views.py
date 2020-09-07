from app import app
from app import database
from flask import request, url_for, redirect, session, render_template
import bcrypt

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        login_user = database.users.find_one({'users': request.form['username']})
        
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
            
                return redirect(url_for('main'))
            return 'Invalid Password <a href="/login">Try again</a>'
        elif database.awaiting_users.find_one({'users': request.form['username']}):
            return 'Awaiting for manual authentication'
        return 'User does not exists do you want to <a href="/register">Register</a>'

    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = database.users.find_one({'users':request.form['username']})
        if existing_user == None:
            if len(request.form['password']) < 63 and len(request.form['password']) > 7:
                hashedpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
           
                database.awaiting_users.insert_one({'users':request.form['username'], 'password': hashedpass})
                return redirect(url_for('login'))
            return 'Please use a password more then 8 characters and less then 63 characters. <a href="/register">Try again.<a>'
        return 'User exists. <a href="/login">Login?<a>'

    elif request.method == 'GET':
        
        return render_template('register.html')
