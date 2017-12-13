from flask_mail import Message
from app import app, mail
from flask import render_template
from config import ADMINS
from .decorators import async


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

'''
Problem:
The problem is that Flask-Mail sends emails synchronously. The web server blocks while the email 
is being sent and only returns its response back to the browser once the email has been delivered 
(slow/offline server = huge problem)

This is a terrible limitation, sending an email should be a background process that does not interfere with the web server
-> use threading/multiprocessing -> allows for send_email function to return immediately
'''

def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed, follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))