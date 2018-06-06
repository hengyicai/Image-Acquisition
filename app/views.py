# -*- encoding: utf-8 -*-

import os
from flask import url_for, redirect, render_template, flash, g, session, Flask, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from forms import ExampleForm, LoginForm
from models import User
from utils import query_db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        print(session.keys())
        user = query_db('select * from userinfo', one=True)
        print(user)
    return render_template('upload.html')


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


# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

# ====================
