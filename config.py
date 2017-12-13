import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [{'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# to send 500 errors via email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'sam.huang2019@gmail.com'
MAIL_PASSWORD = 'queens1205'

# administrator list
ADMINS = ['sam.huang2019@gmail.com']

# pagination
POSTS_PER_PAGE = 3