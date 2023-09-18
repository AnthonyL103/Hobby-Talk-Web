from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
#secure a password so your never storing a password in plain text, using hashing function which has no inverse
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#functions to log in our user, this is why we needed userMixin so we can use the current user object to access all the current information about the user
from flask_login import login_user, login_required, logout_user, current_user
#creates a new blueprint for our login webpage
auth = Blueprint('auth', __name__)
#initliazes 3 authentication functions/routes for our auth blueprint that lets user login, signup, and logout
#methods=[get,post[] makes it so this route can accept these types of requests
#by default we can onyl accept get requests
@auth.route('/login', methods=['GET','POST'])
def login():
     #import request, and set data to request.form so we can get all the data sent to this route's/webpages form
     if request.method == 'POST':
          email = request.form.get('email')
          password = request.form.get('password')
          #what you do when you are looking for a specific entry in ur database
          user = User.query.filter_by(email=email).first()
          if user:
               #checks if the hashes are the same then the user is logged in successfully
               if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    #use remember to remember the user while web server is running
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
               else:
                    flash('Incorrect password, try again.', category='error')
          else:
               flash('Email does not exist.', category='error')
     
     
     return render_template("login.html", user=current_user)

@auth.route('/logout')
#makes sure we cannot access this route unless user is logged in
@login_required
def logout():
    logout_user()
    #redirect to sign up after user is logged out
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
     #makes it so we cna differentiate between a get and poist request
     if request.method == 'POST':
          #gets all the inputed data based on the form label
          email = request.form .get('email')
          firstname = request.form.get('firstname')
          password1 =request.form.get('password1')
          password2 = request.form.get('password2')
          user = User.query.filter_by(email=email).first()
          if user:
               flash('Email already exists.', category = 'error')

          #sets some parameters for user input by using basic python if statements
          elif len(email) < 4:
               #importing flash and using it allows us to flash a message briefly after a specific action has been taken
               #set flash message category so we know what kind fo message it is and we will use it later to set diff styles or formatting to the message
               flash('Email must be greater than 3 characters.', category = 'error')
          elif len(firstname) < 2:
               flash('First name must be greater than 1 characters.', category = 'error')
          elif password1 != password2:
               flash('Passwords must be identical', category = 'error')
          elif len(password1) < 7:
               flash('Password must be greater than 6 characters', category = 'error')
          else:
               #sha265 is a hashing algorithim
               #defines user
               new_user = User(email = email, first_name = firstname, password=generate_password_hash(password1, method='sha256'))
               db.session.add(new_user)
               db.session.commit()
               login_user(user, remember=True)
               flash('Account created successfully!',category='success')
               #redirects user to home after they log in
               return redirect(url_for('views.home'))

     
     return render_template("signup.html", user = current_user)