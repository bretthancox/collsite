from flask import render_template, jsonify, request, g, redirect, url_for, flash, session
from app import app
from werkzeug.local import LocalProxy
from .formBase import bookingForm, loginForm
import boto3
import sys
from flask_bcrypt import Bcrypt

dynamo_object = boto3.resource('dynamodb')

dynamo_confirmed = dynamo_object.Table('confirmed_events')

dynamo_unconfirmed = dynamo_object.Table('unconfirmed_events')

dynamo_users = dynamo_object.Table('users')

bcrypt = Bcrypt(app)

app.secret_key = 'wooo4a9secreT98KeY' 


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = bookingForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']
        booking_date = request.form['booking_date']
        booking_time = request.form['booking_time']
        booking_request = booking_date + ' ' + booking_time
        flash(type(dynamo_confirmed))
        dynamo_unconfirmed.put_item(
            Item={
                 'name': name,
                 'email': email,
                 'booking_request': booking_request})
    elif form.validate() is False:
        flash(form.errors)
    else:
        flash('Testing')
    
    return render_template("index.html",
                           title='Home',
                           form=form)


@app.route("/create", methods=['GET', 'POST'])
def add_user():
    user_form = loginForm(request.form)
    if request.method == 'POST':# and user_form.validate():
        new_user = request.form['username']
        new_password = request.form['password']
        encrypted_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        dynamo_users.put_item(Item={'username': new_user, 'password': encrypted_password})
    else:
        pass
    return render_template("create.html",
                           title='Create account',
                           form=user_form)



#def write_user(uname, pword):
#    dynamo_users.put_item(
#        Item={
#             'username': uname,
#             'password': pword})



@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = loginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = request.form['username']
        testpassword = request.form['password']
        userlist = dynamo_users.scan()
        for users in userlist['Items']:
            if users['username'] == username.lower():
                #if bcrypt.check_password_hash(testpassword, users['password']):
                #    session['username'] = username.lower()
                #    session['access'] = users['access_level']
                #    return render_template('logged_in.html',
                #                           title='Welcome',
                #                           username=username.lower())
                print("Found user")
            else:
                return render_template('login.html',
                                       title='Sign In Failed',
                                       form=login_form)

    user_set = dynamo_users.scan()
    user_dict = []
    for usrs in user_set['Items']:
        user_dict.append(usrs)
    return render_template('login.html', 
                           title='Sign In',
                           form=login_form,
                           usirs=user_dict)
#check https://stackoverflow.com/questions/19141073/rendering-a-python-dict-in-jinja2-werkzeug for info about using a list of dicts correctly

                          

@app.route('/_getBookings', methods=['GET'])
def getBookings():  # bookingsImprove preps unique keys for each record
    bookings_list = []
    all_confirmed = dynamo_confirmed.scan()
    for bookings in all_confirmed['Items']:
        if 'Test' in bookings['nameMask']:
            pass
        elif 'bookingEnd' in bookings.keys():
            bookings_list.append({'title': bookings['nameMask'], 'start': bookings['booking'], 'end': bookings['bookingEnd']})
        else:
            bookings_list.append({'title': bookings['nameMask'], 'start': bookings['booking']})
    return jsonify(bookings_list)


#@app.route('/_addToDb', methods=['PUT'])
#def saveBookings():

@app.route('/about')
def aboutPage():
    return render_template('about.html', title='About')

