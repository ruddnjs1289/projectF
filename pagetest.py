
from flask import *
from flask_migrate import Migrate
from adminpage import member
from model import memberinfo,smoketime,worktime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://root:1234@127.0.0.1:3306/example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]='mysecret'

migrate=Migrate


@app.route('/test')
def test():
 print('function')
   
 
    
 return render_template('test.html')



@app.route('/test2')
def test2():
 print('function')
   
 
    
 return render_template('test2.html')
    
    
app.run(debug=True) 