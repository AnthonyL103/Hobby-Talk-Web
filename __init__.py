from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#imports alchemy which allows us to create our website databse
#assigns databse to an object and a name
db = SQLAlchemy()
DB_NAME = "databse.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'feiruhfieur'
    #register blueprints with flask so it knows we have some webpages with different urls
    from .views import views
    from .auth import auth
    #defining webpage prefix as / meaning you don't want a prefix
    #so if you wanted to access the roots you would have to prefix whatever you said in the route with your set url prefix
    #example: if url_prefix = /auth/ and auth.route("hello") to access roote it would be /auth/hello
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    return app