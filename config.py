import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

# Get the database URL from environment variables or use the default Supabase URL
database_url = os.getenv("DATABASE_URL")

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url + "?sslmode=require"

db = SQLAlchemy(app)
