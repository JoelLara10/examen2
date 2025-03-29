import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'examen.crwe44myk6bg.us-east-2.rds.amazonaws.com')
    DB_USER = os.getenv('DB_USER', 'admin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'Joel1234')
    DB_NAME = os.getenv('DB_NAME', 'examen')
