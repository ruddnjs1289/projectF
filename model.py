from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class memberinfo(db.Model):
    __tablename__ = 'memberinfo' 
    
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50))
    age=db.Column(db.Integer)
    department=db.Column(db.String(50))
    rank=db.Column(db.String(50))
    
    worktimes =db.relationship("worktime", back_populates="memberinfos")
    
    
class smoketime(db.Model):
    __tablename__ ='smoketime'
    
    cnt=db.Column(db.Integer, primary_key=True,autoincrement=True)
    smId=db.Column(db.Integer,db.ForeignKey('worktime.id'))
    startsmoke=db.Column(db.DateTime)
    endsmoke=db.Column(db.DateTime)
    smokesum=db.Column(db.Integer)
    
    worktimes =db.relationship("worktime", back_populates="smoketimes")
    
    def __init__(self,smId=None,startsmoke=None,endsmoke=None,smokesum=None):
        self.smId=smId
        self.startsmoke=startsmoke
        self.endsmoke=endsmoke
        self.smokesum=smokesum
        
class worktime(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    picture=db.Column(db.String(100))
    workid=db.Column(db.Integer,db.ForeignKey('memberinfo.id'))
    workstart=db.Column(db.DateTime)
    workend=db.Column(db.DateTime)
    
    smoketimes =db.relationship("smoketime", back_populates="worktimes")
    memberinfos =db.relationship("memberinfo", back_populates="worktimes")
    
    def __init__(self,Id=None,picture=None,workid=None,workstart=None,workend=None): 
        self.id=Id
        self.picture=picture
        self.workid=workid
        self.workstart=workstart
        self.workend=workend