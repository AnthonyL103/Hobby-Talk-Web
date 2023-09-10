from flask import Blueprint, render_template, request, flash
#creates a new blueprint for our login webpage
auth = Blueprint('auth', __name__)
#initliazes 3 authentication functions/routes for our auth blueprint that lets user login, signup, and logout
#methods=[get,post[] makes it so this route can accept these types of requests
#by default we cna onyl accept get requests
@auth.route('/login', methods=['GET','POST'])
def login():
     #import request, and set data to request.form so we can get all the data sent to this route's/webpages form
     data= request.form
     print(data)
     return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
     #makes it so we cna differentiate between a get and poist request
     if request.method == 'POST':
          #gets all the inputed data based on the form label
          email = request.form .get('email')
          firstname = request.form.get('firstname')
          password1 =request.form.get('password1')
          password2 = request.form.get('password2')
          #sets some parameters for user input by using basic python if statements
          if len(email) < 4:
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
               flash('Account created successfully!',category='success')


     
     return render_template("signup.html")