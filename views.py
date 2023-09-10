#create a root (pages for user to go too)
#renders template, so we just import render_template
from flask import Blueprint, render_template
#use bluprint to create webpages, sets views to web page section
views = Blueprint('views', __name__)
#this function will run whenever we go to the / root
#root lets you set the custom urls for webpages
@views.route('/')
def home():
    #return test as an h1 tag
    #return render template and the name of our html template that we want to use
    return render_template("home.html")


