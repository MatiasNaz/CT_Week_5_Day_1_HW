from flask import Blueprint
from flask import render_template

# import forms
from .forms import UserInfoForm


# create instance of blueprint
auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login')
def logMeIn():
    return render_template('login.html')

@auth.route('/signup')
def signMeUp():
    my_form = UserInfoForm()
    return render_template('signup.html', form = my_form )



