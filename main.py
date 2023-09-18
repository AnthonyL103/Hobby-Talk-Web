from Website import create_app
import os
#imports create_app from Website which creates an application for the entire program 
app = create_app()

# Configure the UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = '/Users/anthonyli/Desktop/WebDevelopmentProject/uploads'  # Replace with the desired directory path

# Ensure the specified directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

#running flask application and we will now have a running web server
#only if we run this final not import 
#for some reason you wanted to import main.py it would run the web server
if __name__=='__main__':
    #auto rerun web server, we don't have to keep manually running web server
    app.run(debug=True)