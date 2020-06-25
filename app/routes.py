from flask import Flask, render_template, flash, redirect
from app import app
from .forms import *
from flask_login import current_user, login_user, logout_user, LoginManager, login_required

login_manager = LoginManager(app)

def checklogin():
    if current_user.is_authenticated:
        return True
    else:
        return False

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', form = form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if username:
            flash('Username Already Taken')
            return (redirect(url_for('signup')))
        if email:
            flash('Email already taken')
            return (redirect(url_for('signup')))
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha512:10000', salt_length=8)
        new_user = User(email=form.email.data, username=form.username.data, full_name = form.full_name.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username
        return redirect(url_for('login'))
    logged_in = checklogin()   
    return render_template("signup.html", form=form, logged_in=logged_in)

@app.route('/profile', methods=['GET', 'POST'])

def create_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        new_profile = Profile()
        new_profile.company = form.company.data
        new_profile.job_title = form.job_title.data
        new_profile.job_title = form.job_title.data
        new_profile.profession = form.profession.data
        new_profile.salary = form.salary.data
        new_profile.bonuses = form.bonuses.data
        new_profile.education = form.education.data
        new_profile.experience = form.experience.data
        new_profile.gender = form.gender.data
        new_profile.sex = form.sex.data
        new_profile.skin_color = form.skin_color.data
        new_profile.ethnicity = form.ethnicity.data
        new_profile.race = form.race.data
        new_profile.orientation = form.orientation.data
        new_profile.age = form.age.data
        new_profile.disability = form.disability.data
        new_profile.veteran = form.veteran.data
        new_profile.exconvict = form.exconvict.data

        db.session.add(new_profile)
        db.session.commit()
        # logged_in = checklogin()
        flash("Your profile has been made!", "success")
        return redirect(url_for('home'))
    logged_in = checklogin()
    return render_template("profile.html", form=form, logged_in=logged_in)



