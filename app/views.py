import gdata

from app import app
from app.db import gd_client, spreadsheet_id, worksheet_id

from flask import request, abort
from flask import render_template
from flask import flash, redirect, url_for

from flask.ext.wtf import Form

from wtforms import StringField, BooleanField
from wtforms import TextField, PasswordField, validators, IntegerField, FormField

from wtforms.widgets import TextArea

from wtforms.validators import DataRequired
from wtforms.validators import Length


class loginForm(Form):
    email_regex = '^[a-zA-Z0-9]+$|^[a-zA-Z0-9]+@gmail.com$'
    firstname = StringField('Firstname', validators = [DataRequired()])
    lastname = TextField('Lastname', validators = [DataRequired()])
    role = TextField('role', validators = [DataRequired()])
    active = TextField('active', validators = [DataRequired()])
    email = TextField('Email', [validators.Regexp(message = 'Incorrect email', regex = email_regex)])
    contact = TextField('Contact', validators = [validators.Regexp(message ='E.g(xxx)xxx-xxxx', regex ='^[0-9]{10}$')])
    address1 = StringField('Address1', widget = TextArea(), validators = [DataRequired(),Length(min = 1, max = 50)])
    address2 = StringField('Address2', widget = TextArea(), validators = [DataRequired(),Length(min = 1, max = 50)])

class submitForm(Form):
    firstname = StringField('Firstname', validators = [DataRequired(), Length(min = 1, max = 20)])
    lastname = TextField('Lastname', validators = [DataRequired(),Length(min = 1, max = 20)])
    role = TextField('role', validators = [DataRequired(),Length(min = 1, max = 20)])
    active = TextField('active', validators = [DataRequired(),Length(min = 1, max = 20)])
    email = TextField('Email', [validators.Email(),Length(min = 1, max = 20)])
    contact = TextField('Contact',validators = [validators.Regexp(message='use this format (xxx)xxx-xxxx', regex='^[0-9]{10}$')])
    address1 = StringField('Address1', widget = TextArea(), validators = [DataRequired(),Length(min = 1, max = 50)])
    address2 = StringField('Address2', widget = TextArea(), validators = [DataRequired(),Length(min = 1, max = 50)])


@app.route('/confirm', methods = ['POST'])
def confirm():
   return render_template('confirm.html', title = 'Confirmation!!!', posts=request.form)


@app.route('/submit', methods = ['POST'])
def entry():
   form = submitForm()
   if form.validate_on_submit() == False:
      #abort(500,"data is wrong.")
      return "data is wrong."
   entry = gdata.spreadsheets.data.ListEntry()
   entry.from_dict(request.form)
   gd_client.add_list_entry(entry,spreadsheet_id,worksheet_id)
   return render_template('submit.html', title = 'Conngratulation!!!', user=request.form['firstname'])


@app.route('/index.html', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        return render_template('confirm.html', title = 'Confirmation!!!', posts=request.form, form = form)
    return render_template('index.html', title = 'Home', form = form)
