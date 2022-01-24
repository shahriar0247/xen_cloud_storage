from flask import Flask, redirect, render_template, request, session, abort, send_from_directory, url_for
import webbrowser
import zipfile
import os
import datetime
import magic



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.secret_key = os.urandom(12)


from app import process_files

from app.setting_dir import temp_dir, main_dir, delete_dir 

from app import ftp_functions


from app import login_views
from app import path_views
from app import upload_download_views


