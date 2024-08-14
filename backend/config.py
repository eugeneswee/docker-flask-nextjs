import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@mysql:3306/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
