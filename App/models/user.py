from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), nullable =False)
    lastName = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(120), nullable=False)
    faculty = db.Column(db.String(80), nullable =True)
    department = db.Column(db.String(80), nullable =True)
    programme = db.Column(db.String(80), nullable =True)
    graduationyear = db.Column(db.Integer, nullable =True)
    job = db.Column(db.String(80), nullable =True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


