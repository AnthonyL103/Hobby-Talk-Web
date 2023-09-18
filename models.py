#create database models for our users and project instructions
from . import db 
#flask login is a module that helps users log in
from flask_login import UserMixin
#imports func which associates data with the time and date it was entered
from sqlalchemy.sql import func
#All Steps need to look like this
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    #what func does is it gets the current date and time, and it will use it to store the data in the date time field
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    #foreign key ius a key that references an id for another column in the databse
    #Saying we must pass an id of an existing user to this field
    #for sql func it is lowercase sensitive which is why it is user when the class is called User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(1000))  # Store the image file path.
    description = db.Column(db.String(255))  # Optional: Store a description of the image.
    upload_date = db.Column(db.DateTime(timezone=True), default=func.now())  # Store the upload date.

    # Add a foreign key to associate the image with a user or note.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))


#All Users need to look like this
class User(db.Model, UserMixin):
    #defines a unique key for each user, and no user can have the same ID or Info
    id = db.Column(db.Integer, primary_key = True)
    #defines email, pswd, and name using a String and whenever you define a string you need to set a max length
    #the unique True makes it so every user has to have a unique email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #for relationship you don't need lowercase
    #associates user with steps
    notes = db.relationship('Note')
    images = db.relationship('Image')


