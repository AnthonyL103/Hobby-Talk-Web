#create a root (pages for user to go too)
#renders template, so we just import render_template
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, current_app
from flask_login import login_required, current_user
from .models import Note, Image  # Import the Image model
from . import db
import os
import json
from werkzeug.utils import secure_filename


#use bluprint to create webpages, sets views to web page section
views = Blueprint('views', __name__)
#this function will run whenever we go to the / root
#root lets you set the custom urls for webpages
@views.route('/', methods=['GET','POST'])
@login_required
def home():
    images = Image.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        note = request.form.get('note')

        if note is not None and len(note) < 1:
            flash('Note is too short', category = 'error')
        elif note is not None:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category = 'success')
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                # Ensure a secure filename and specify the upload directory
                filename = secure_filename(image.filename)
                upload_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image.save(upload_dir)

                # Create a new Image object and store the image information in the database
                new_image = Image(file_path=upload_dir, user_id=current_user.id)
                db.session.add(new_image)
                db.session.commit()
                flash('Image uploaded successfully!', category='success')
            else:
                flash('Image file invalid, please try again', category='error')

        return redirect(url_for('views.home'))
    #return render template and the name of our html template that we want to use
    #user=curr_user is used to reference current user and check if its authenticated, so we can display the right options based on authentication
    return render_template("home.html", user=current_user, images=images)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    #request is going to come as the data paramter of the request object
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    #check if note exists
    if note:
        #if user actually owns this note
        if note.user_id == current_user.id:
            #this is how you delete an object, you query it and you put it inside of the delete
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

