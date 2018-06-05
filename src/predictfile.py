import os
from flask import Flask, request, redirect, url_for  # redirectはページ遷移に使う
from werkzeug.utils import secure_filename # アップロードされたファイル名に危険なコマンドが含まれている場合それを除去する


UPLOAD_FOLDER = './uploads'
ALLOWD_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowd_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWD_EXTENSIONS
