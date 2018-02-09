from flask import render_template, jsonify, request, g, redirect, url_for, flash
from app import app
#from .forms import LoginForm
#from flaskext.couchdb import CouchDBManager, Document, TextField, DateField, BooleanField
from werkzeug.local import LocalProxy
from .formBase import bookingForm



#@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = bookingForm(request.form)
    
    print(form.errors)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']
        booking_date = request.form['booking_date']
        booking_time = request.form['booking_time']
        flash(name + ' ' + email + ' ' + booking_date + ' ' + booking_time)
    elif form.validate() is False:
        flash(form.errors)
    else:
        flash('Testing')
    
    return render_template("index.html",
                           title='Home',
                           form=form)


                          

@app.route('/_getBookings', methods=['GET'])
def getBookings():  # bookingsImprove preps unique keys for each record
    bookingsImprove = []  #dict for next step
    bookingsImprove.append({'title': 'A TITLE', 'start': 'Nov 7 2017 15:20:00'})
    return jsonify(bookingsImprove)
    #return bookingsImprove


@app.route('/about')
def aboutPage():
    return render_template('about.html', title='About')
