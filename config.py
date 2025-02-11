import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

# Get the database URL from environment variables or use the default Supabase URL
db_url = os.getenv("DATABASE_URL", "postgresql://postgres:[YOUR-PASSWORD]@db.twplccttrbfxpvafykqi.supabase.co:5432/postgres")

# Ensure SSL mode is enabled for Supabase connections
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)  # Render sometimes uses 'postgres://'

# app.config["SQLALCHEMY_DATABASE_URI"] = db_url + "?sslmode=require"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_url = "postgresql://postgres:-Fxb.hy@U-6jQs@@db.twplccttrbfxpvafykqi.supabase.co:5432/postgres"

db = SQLAlchemy(app)
