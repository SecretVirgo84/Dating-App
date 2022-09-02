from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    email = db.Column(db.Text, nullable = False, unique = True)
    birthdate = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    gender = db.Column(db.Text, nullable = False)

    db.Column(
        'date_joined', db.DateTime,
        default = datetime.datetime.utcnow
    )

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    details = db.Column(db.Text)
    pic = db.Column(db.Boolean)
    gender_interest = db.Column(db.Text, nullable = False)

    def serialize(self):
        return{
            'id': self.id,
            'gender_interest': self.gender_interest
        }

class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    messages = db.Column(db.Text)
    user_profile = db.Column(db.Text)



