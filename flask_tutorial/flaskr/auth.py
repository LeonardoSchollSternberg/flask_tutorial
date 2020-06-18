'''---3---'''
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

arq_playlist=0

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    
    return wrapped_view

'''--TRENSURB--'''
@bp.route('/teste')
def teste():
    return render_template('auth/mon_hor.html')

@bp.route('/teste2')
def teste2():

    #if 'i' not in locals():
    #    i=0
    #    print(i)
    #else:
    #    i=i+1
    #    print(i)

    global arq_playlist

    arr = {}
    f = open("playlist.txt", "r")
    f1 = f.readlines()
    for l1 in f1:
        text1 = l1.split(";")
        for l2 in text1:
            pointer = l2.split(",")[0]
            text2 = l2.split(",")[1]
            delay = l2.split(",")[2]
            arr[pointer] = text2, delay
    f.close()

    if ((arr['{}'.format(arq_playlist)][0].split('.')[1])=="png") or ((arr['{}'.format(arq_playlist)][0].split('.')[1])=="jpg"):
        print("Foi enviado: "+arr['{}'.format(arq_playlist)][0]+", com delay "+ arr['{}'.format(arq_playlist)][1])
    elif ((arr['{}'.format(arq_playlist)][0].split('.')[1])=="mp4") or ((arr['{}'.format(arq_playlist)][0].split('.')[1])=="ogg"):
        print("Foi enviado: "+arr['{}'.format(arq_playlist)][0])
    else:
        print("Foi enviado: ERRO")
    
    data = arr['{}'.format(arq_playlist)]

    if(arq_playlist < len(arr)-1):
        arq_playlist=arq_playlist+1
    else:
        arq_playlist=0

    return render_template('auth/pagina_teste5.html', data=data)