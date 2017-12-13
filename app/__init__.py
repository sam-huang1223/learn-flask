from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask_mail import Mail

mail = Mail(app)

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

# if in production mode, email errors to backend admin
'''
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
'''

# if in production mode, log errors to tmp folder
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

from app import views, models
# views imports the variables defined above




