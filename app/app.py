from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_migrate import Migrate
import os
import traceback
from flask_restx import Api




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/backend_challenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()    