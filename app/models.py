from datetime import datetime
from app import db

#USER

class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Interger, primary_key=True, index=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db. Column(db.String(100), unique=True, index=True, nullable=False)

    posts = db.relationship('Post', back_populates='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


#POST

class Post(db.model):
    __tablename__ = "posts"

    id = db.Column(db.Interger,primary_key=True, index=True)
    title = db.Column(db.String(100), index=True, nullable=False) 
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.datetime, default=datetime.utcnow)
    author_id = db.Column(db.Interger, db.ForeignKey('users.id'),nullable=False)    

    author = db.relationship('User', back_populates = 'posts')  

    comments = db.relationship('Comment', back_populates = 'post', lazy = 'dynamic') 

    def __repr__(self):
        return f'<Post {self.title}>'


#COMMENT

class Comment(db.model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, index=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    post = db.relationship('Post', back_populates='comments')

    def __repr__(self):
        return f'<Comment {self.id}>'        
