from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Reptile(db.Model):
    __tablename__ =  'reptiles' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(250))
    common_name = db.Column(db.String(250))
    scientific_name = db.Column(db.String(250))
    conservation_status = db.Column(db.String(250))
    native_habitat = db.Column(db.String(250))
    fun_fact = db.Column(db.Text) 