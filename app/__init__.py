from flask import Flask, redirect,request, session
import datetime
import SETTINGS


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['SECRET_KEY'] = SETTINGS.FLASK.secret_key


from app import process_files

from app.setting_dir import temp_dir, main_dir, delete_dir 

from app import ftp_functions


from app.views.login import login_views
from app import path_views
from app import upload_download_views


@app.before_request
def before_request_app():


    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=30)
    session.modified = True
    if request.endpoint != "login" and request.endpoint != "static" and request.endpoint != "signup":
        try:
            if session['username']:
                pass
            else:
                return redirect("/login") 
        except:
            return redirect("/login") 

