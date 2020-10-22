##IMPORTS

from application import app
from flask import request, render_template, redirect, flash, session #imports for various flask functions
from os import urandom #generating salt
import hashlib #library for hashing
from application.helper_functions import *

###LOGIN THE USER
@app.route('/login/', methods=['POST'])
def login():
	# get form information
	formData = request.form
	
	# validation
	if formData['username'] == "":
		flash("The username field is required.")
		return redirect("/")
	if formData['password'] == "":
		flash("The password field is required.")
		return redirect("/")

	#get data from database
	data = query_db("SELECT password,  isTeacher, id FROM people WHERE username=? LIMIT 1", [formData['username']])
	#make sure username is right
	if data == []:
		flash("Your username was incorrect.")
		return redirect("/")

	# check the password	
	if data[0][0] == formData['password'].encode():
		#correct password
		session['isTeacher'] = data[0][1]
		session['id'] = data[0][2]
		#if student, redirect to students page
		if session['isTeacher'] == 0:
			return redirect("/students/")
		#else they are a teacher, redirect to teachers page
		else:
			return redirect("/teachers/")

	flash("Your password was incorrect.")
	return redirect("/")

###REGISTER THE USER
@app.route('/register/', methods=['GET', 'POST'])
def register():
	
	#form data is GET, so render template
	if request.method == 'GET':
		return render_template('register.html')

	#request method is POST, so do everything
	
	formData = request.form
	
	#form validation
	if formData['username'] == "" or formData['password'] == "" or formData['name'] == "" or formData['email'] == "":
		return "All text fields are required"
	if not 'isTeacher' in formData: #if is teacher wasn't selected
		isTeacher = 0 #they aren't a teacher...
	else:
		isTeacher = 1 #they are a teacher!
	
	password = formData['password'].encode()
	execute_db("INSERT INTO people (isTeacher, username, password, name, email) VALUES (?, ?, ?, ?, ?)", [isTeacher, formData['username'], password,  formData['name'], formData['email']])
	flash("The entry was created")
	return redirect("/register/")
