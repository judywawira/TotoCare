import json , ast
from bson.json_util import dumps
from bson import json_util

from app import app, lm , mongo, mongo2, client, db
from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from flask import jsonify

from .forms import LoginForm, StudentRegistrationForm , IncidentForm
from .user import User

#Describe Minor problem behaviour
minor = ['Defiance','Disrespect','Physical Contact','Tardy','Inappropriate Language','Property Misues',
'Dress Code','Electronic Violation','Other']

major = ["Defiance",'Disrespect','Abusive Language','Harassment','Fighting','Electronic Violation','Property Damage',
'Lying/Cheating','Dress Code','Inappropriate display of affection','Other']

motivation = ['Peer attention','Adult attention','Item/Activity avoid','Peer attention','Adult attention','Item/Activity']

action_taken = ['Time out/detention','Conference with student','Loss of privileges','Parent contact','Individualized instruction',
'In-school suspension','Out-of-school suspension','Action pending','Other']

others_involved = ['None','Peers','Teacher','Staff','Subtitute','Unknown','Other']

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
        grade = form.grade.data

        db.students.insert({
            'firstname':firstname,'middlename':middlename,'lastname':lastname,'studentid':studentid,'grade':grade,
            'address1':address1,'address2':address2,'zipcode':zipcode,'state':state
        })
        
        return redirect('/')

@app.route('/teacher',methods=['GET'])
@login_required
def view_teacher():
    teachers = mongo2.db.teachers.find()
    return render_template('teacher.html',title='List of teachers',
    teachers = teachers)

@app.route('/incident',methods=['GET'])
@login_required
def incident_report():
    form = IncidentForm()

    locations = mongo2.db.locations.find()

    return render_template('incident.html', title = 'Incident Report',
        locations=locations,
        minor = minor,
        major = major,form = form)

@app.route('/incident',methods=['POST'])
@login_required
def view_incident_report():
    form = IncidentForm()
    if request.method == 'POST':
        location = form.location.data
        minor = request.form.getlist('minor')
        major = request.form.getlist('major')
        motivation = request.form.getlist('motivation')
        action = request.form.getlist('action')
        others = request.form.getlist('others')

        db.incident.insert({
            'location':location,
            'minor_problem_motivation': minor,
            'major_problem_motivation':major,
            'possible_motivation':motivation,
            'action_taken':action,
            'others_involved':others
        })
    return redirect('/')

@app.route('/locations',methods=['GET'])
@login_required
def locations():
    locations = mongo2.db.locations.find({})
    return render_template('locations.html',
        locations=locations)
  
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
Used to reload the user object through different sessions by taking 
the unicode ID of user , returning the user object and if the user ID is invalid returns None 
"""
@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])