from app import app, lm
from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm,StudentRegistrationForm
from .user import User

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.TotoCare

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)    

@app.route('/student', methods=['POST'])
@login_required
def newstudent():
    form = StudentRegistrationForm()
    if request.method == 'POST':
        firstname = form.firstname.data
        middlename = form.middlename.data
        lastname = form.lastname.data
        studentid = form.studentid.data
        #DOB = form.DOB.data
        address1 = form.address1.data
        address2 = form.address2.data
        zipcode = form.zipcode.data
        state = form.state.data

        db.students.insert({
            'firstname':firstname,'middlename':middlename,'lastname':lastname,'studentid':studentid,
            'address1':address1,'address2':address2,'zipcode':zipcode,'state':state
        })
        
        return redirect('/')
  
@app.route('/student', methods=['GET'])
@login_required
def studentpage():
    form = StudentRegistrationForm()
    return render_template('student.html',title = 'New Student Registration',form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    return render_template('write.html')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings.html')



"""
USed to reload the user object through different sessions by taking 
the unicode ID of user , returning the user object and if the user ID is invalid returns None 
"""
@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])