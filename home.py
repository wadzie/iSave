from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField,  validators
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


# User's profile once logged in
@app.route('/profile')
def profile():
    return render_template('profile.html')


class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():

        flash("Login was successful", 'success')
        return redirect(url_for('profile'))

    return render_template('login.html', form=form)


class RegistrationForm(Form):
    first_name = StringField('Name', [validators.Length(min=1, max=25)])
    last_name = StringField('Last Name', [validators.Length(max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    phone_number = StringField('Phone Number', [validators.Length(max=10)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    accept_tos = BooleanField('I accept the Terms and conditions', validators=[InputRequired()])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering, you can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
