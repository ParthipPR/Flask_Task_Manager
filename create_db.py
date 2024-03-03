from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app, db

    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()