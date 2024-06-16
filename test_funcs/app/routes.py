from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from .models import User
from . import db, login_manager

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.index'))

@main.route('/authorize')
def authorize():
    # OAuth2.0 authorization flow
    pass

@main.route('/callback')
def callback():
    # Handle the callback from Google's OAuth 2.0 server
    pass

@main.route('/dashboard')
@login_required
def dashboard():
    return "Welcome to your dashboard!"
