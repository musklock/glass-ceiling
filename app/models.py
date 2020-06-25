from app import db
from flask_login import current_user, login_user, logout_user
from flask_login import UserMixin, login_required

class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(15), unique=True, nullable = False)
    full_name = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(60), nullable=False)
    # otp_secret = db.Column(db.Integer, nullable=True)
    profile = db.relationship('User_Profile', backref='author_of_profile', lazy=True)

class Profile(db.Model):
    __tablename__ = "Profiles"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    company = db.Column(db.String(50), nullable = False)
    job_title = db.Column(db.String(50), nullable = False)
    profession = db.Column(db.String(50), nullable = False)
    salary = db.Column(db.String(50), nullable = False)
    bonuses = db.Column(db.String(50), nullable = False)
    education = db.Column(db.String(50), nullable = False)
    experience = db.Column(db.String(50), nullable = False)
    gender = db.Column(db.String(50), nullable = False)
    sex = db.Column(db.String(50), nullable = False)
    skin_color = db.Column(db.String(50), nullable = False)
    ethnicity = db.Column(db.String(50), nullable = False)
    race = db.Column(db.String(50), nullable = False)
    orientation = db.Column(db.String(50), nullable = False)
    age = db.Column(db.String(50), nullable = False)
    disability = db.Column(db.String(50), nullable = False)
    veteran = db.Column(db.String(50), nullable = False)
    exconvict = db.Column(db.String(50), nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
