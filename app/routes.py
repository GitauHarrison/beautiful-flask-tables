from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, AdminForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Admin, User


@app.route('/')
@app.route('/index')
@login_required
def index():
    admins = Admin.query.all()
    return render_template('index.html', title='Home', admins=admins)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>/admin')
@login_required
def admin(username):
    user = User.query.filter_by(username=current_user.username).first_or_404()
    form = AdminForm()
    if form.validate_on_submit():
        admin = Admin(
            username=form.username.data,
            email=form.email.data,
            age=form.age.data,
            address=form.address.data,
            phone=form.phone.data
            )
        db.session.add(admin)
        db.session.commit()
        flash('You have added a new admin')
        return redirect(url_for('index'))
    return render_template('adminform.html',
                           user=user,
                           form=form
                           )
