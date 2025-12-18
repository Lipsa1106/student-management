import os
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:336633@localhost:5432/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-secret")
