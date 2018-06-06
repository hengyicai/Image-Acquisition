# -*- encoding: utf-8 -*-

import os
from flask import url_for, redirect, render_template, flash, g, session, Flask, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from forms import ExampleForm, LoginForm
from models import User
from utils import query_db, tail
from flask import jsonify
import logging

LOG_FILE = 'app/log/app.log'
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/user_login', methods=['POST'])
def user_login():
    params = request.form
    user_name = params.get('username')
    passwd = params.get('pwd')
    query_res = query_db("SELECT * FROM userinfo WHERE username=?", args=(user_name,), one=True)
    if query_res is not None and query_res['pwd'] == passwd:
        response = {
            'code': 0,
            'msg': 'success!'
        }
        session['username'] = user_name
        logger.info('{} log in success!'.format(user_name))
    else:
        response = {
            'code': 1,
            'msg': 'user does not exist!'
        }
        logger.warning('{} attempt to log in the system with the wrong password!'.format(user_name))
    return jsonify(response)


@app.route('/user_logout', methods=['POST'])
def user_logout():
    logger.info('{} log out the system!'.format(session['username']))
    del session['username']
    return jsonify({
        'code': 0,
        'msg': "success"
    })


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        upload_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
        f.save(upload_path)
        if 'username' in session:
            logger.info('{} upload file {} to {}'.format(session['username'], f.filename, app.config['UPLOADED_PATH']))
        else:
            logger.warning('some one upload file {} to {} without login!'.format(
                f.filename,
                app.config['UPLOADED_PATH']
            ))
    return render_template('upload.html')


@app.route('/tail_log', methods=['POST'])
def tail_log():
    log_content = ''
    if os.path.exists(LOG_FILE):
        log_content = tail(LOG_FILE)
    response = {
        'code': 0,
        'msg': log_content
    }

    return jsonify(response)


@app.route('/list/')
def posts():
    return render_template('list.html')


@app.route('/save/', methods=['GET', 'POST'])
@login_required
def save():
    form = ExampleForm()
    if form.validate_on_submit():
        print "salvando os dados:"
        print form.title.data
        print form.content.data
        print form.date.data
        flash('Dados salvos!')
    return render_template('new.html', form=form)


@app.route('/view/<id>/')
def view(id):
    return render_template('view.html')
