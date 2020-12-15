"""SQLAlchemy models and utility functions for Twitoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    #primary id column
    id = DB.Column(DB.BigInteger, primary_key=True)
    #name column
    name = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)

# Tweet Table
class Tweet(DB.Model):
    # primary id column
    id = DB.Column(Db.BigInteger, primary_key=True)
    # text column of character length 300 (unicode)
    text = DB.Column(DB.Unicode(300))
    # foreign key - user id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))