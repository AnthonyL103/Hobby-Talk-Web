from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#imports path from operating system to check if our databse exists
from os import path
from flask_login import LoginManager
#imports alchemy which allows us to create our website databse
#assigns databse to an object and a name
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'feiruhfieur'
    #This will store this database in the website folder
    #when you use an f string it can be python code and it wil be evaluated as as tring
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initialize database, by taking the databse we defined and tell the program this is the app we are going to use for the database
    db.init_app(app)

    
    #register blueprints with flask so it knows we have some webpages with different urls
    from .views import views
    from .auth import auth
    
    #defining webpage prefix as / meaning you don't want a prefix
    #so if you wanted to access the roots you would have to prefix whatever you said in the route with your set url prefix
    #example: if url_prefix = /auth/ and auth.route("hello") to access roote it would be /auth/hello
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    #we need to make sure we load this model file and defines the classes inside it for us before we create the databse
    from .models import User, Note
    #check if data base exists and if not it will create it
    with app.app_context():
        db.create_all()
        print('Created Database')
    
    login_manager = LoginManager()
    #where should flask redirect when user isn't logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    #telling flask how to load a user by passing in the unique id we created for every user when they signed up 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
  
    return app

