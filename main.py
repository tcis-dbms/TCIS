from flask import Flask,render_template,request,redirect,session
from flask import url_for
import os
# import MySQLdb as mysql
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,logout_user,LoginManager 
from werkzeug.security import check_password_hash, generate_password_hash


  
  
  #my db connection
local_server=True
app = Flask(__name__)
app.secret_key="banuprakash"
# syntax to connect database "app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/db_name'"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/TCIS'

db=SQLAlchemy(app)


class Signup(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    password=db.Column(db.String(100))
    # age=db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    try:
        Signup.query.all()
        return 'My database is connected'
    except:
        return 'not connected'

@app.route('/crdIssue')
def crdIssue():
    return render_template('crdIssue.html')

@app.route('/crdTyp')
def crdTyp():
    return render_template('crdTyp.html')

@app.route('/chkBal')
def chkBal():
    return render_template('chkBal.html')

@app.route('/crdRechrg')
def crdRechrg():
    return render_template('crdRechrg.html')

@app.route('/tollBooth')
def tollBooth():
    return render_template('tollBooth.html')

@app.route('/tollCollection')
def tollCollection():
    return render_template('tollCollection.html')

@app.route('/vcleTyp')
def vcleTyp():
    return render_template('vcleTyp.html')
    

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        # return render_template('chkBal.html')
        username=request.form.get('username')
        password=request.form.get('password')
        user=Signup.query.filter_by(id=username,password=password).first()
        if user:
            # login_user(user)
            return redirect(url_for('index'))
        else:
            print(username,password)
            print("Invalid credentials")
            return render_template('login.html')
                
    return render_template('login.html')

    


app.run(debug=True)