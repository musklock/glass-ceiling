from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Email, Length, Required, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField("Username", validators=[InputRequired(), Length(min=2, max=20)])
    full_name = StringField("Full Name", validators=[InputRequired(), Length(min=5, max=35)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=128)])
    password_again = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("SignUp")
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class ProfileForm(FlaskForm):
    company = StringField('Company', validators=[InputRequired()])
    job_title = StringField("Job Title", validators=[InputRequired()])
    profession = TextAreaField("Profession", validators=[Length(max=1024)])
    salary = StringField('Email', validators=[InputRequired(), Email()])
    bonuses = StringField('Bonuses', validators=[InputRequired()])
    education = StringField('Education', validators=[InputRequired()])
    experience = TextAreaField('Experience', validators=[InputRequired()])
    gender = StringField('Gender', validators=[InputRequired()])
    sex = StringField('Sex', validators=[InputRequired()])
    skin_color = StringField('Skin Color', validators=[InputRequired()])
    ethnicity = StringField('Ethnicity', validators=[InputRequired()])
    race = StringField('Race', validators=[InputRequired()])
    orientation = StringField('Orientation', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    disability = StringField('Disability', validators=[InputRequired()])
    veteran = StringField('Veteran', validators=[InputRequired()])
    exconvict = StringField('Ex-convict', validators=[InputRequired()])
    submit = SubmitField('Submit')


    
class RequestResetForm(FlaskForm):
    email = StringField('Please Enter your Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No account with that email exists!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')