from flask import render_template, jsonify, request, g, redirect, url_for, flash
from app import app
from flaskext.couchdb import CouchDBManager, Document, TextField, DateField, BooleanField
from werkzeug.local import LocalProxy

manager = CouchDBManager()  #instantiate
manager.setup(app)  #start

class NewBooking(Document):  #class for interrogating CouchDB
    book_name = TextField()
    book_email = TextField()
    book_date = TextField()
    book_time = TextField()
    book_confirmation = BooleanField(default=False)
    
class approvedBooking(Document):  #class for interrogating CouchDB
    book_name = TextField()
    book_email = TextField()
    book_date = TextField()
    book_time = TextField()
    book_confirmation = BooleanField(default=False)
