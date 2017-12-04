from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'  # for below to work Flask-Login needs to know what view logs users in
'''
Let's say you navigate to a page that requires you to be logged in, but you aren't just yet. 
In Flask-Login you can protect views against non logged in users by adding the login_required decorator. 
If the user tries to access one of the affected URLs then it will be redirected to the login page automatically. 
Flask-Login will store the original URL as the next page, and it is up to us to return the user to this page 
once the login process completed.
'''
from app import views, models
# views imports the variables defined above



