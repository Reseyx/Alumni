from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from models.user import db, User
from models.forms import SignUp, LogIn, SearchForm

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

''' End Flask Login Functions '''

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  login_manager.init_app(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''

@app.route('/', methods=['GET'])
def index():
  form = LogIn()
  return render_template('login.html', form=form)

#user submits the login form
@app.route('/login', methods=['POST'])
def loginAction():
  form = LogIn()
  
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(email = data['email']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return redirect(url_for('Index.html')) # redirect to main page if login successful
  flash('Invalid credentials')
  return redirect(url_for('signup.html'))


@app.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template

@app.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    userdata = request.form # get data from form submission
    newuser = User(firstName=userdata['firstname'], 
      username = userdata['username'],
      lastName=userdata['lastname'],
      email = userdata['email'],
      graduationyear=userdata['graduationyear'],
      programme=userdata['programme'],
      department=userdata['department'],
      faculty=userdata['faculty'],
      job=userdata['currentjob'])
    newuser.set_password(userdata['password']) # create user object
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('Index.html'))# redirect to hompage
  flash('Error invalid input!')
  return redirect(url_for('signup')) 





#@app.route('/logout', methods = ['GET'])
#@login_required
#def logout():
#  logout_user()
#   return redirect(url_for('login.html'))

#@app.route('/posts')
#def user():
	# Grab all the posts from the database
#	user = Users.query.order_by(Posts.date_posted)
#	return render_template("posts.html", posts=posts)

@app.context_processor
def base():
  form = SearchForm()
  return dict(form=form)

@app.route('/search', methods=['POST'])
def search():
  
  form=SearchForm()
  users = User.query
  if form.validate_on_submit():
    user = form.searched.data

    users= users.filter(User.faculty.like('%' + user + '%'))
    users= users.order_by(User.lastname).all()
    return render_template('search.html', form=form, searched=user)
    
  

app.run(host='0.0.0.0', port=8080, debug = True)
