import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3306/project")
Base = declarative_base()

'''class Employee(Base):
    __tablename__ = 'employee2'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    
    Base.metadata.create_all(engine)'''

class Visits(Base):
    __tablename__ = 'visits'
    VisitTime=sqlalchemy.Column(Date,primary_key=True)
    picture=sqlalchemy.Column(sqlalchemy.String(length=200))
    name=sqlalchemy.Column(sqlalchemy.String(length=50))
    
    Base.metadata.create_all(engine)
    
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
    
    
'''newEmployee = Employee(id=1,first_name="Rob", last_name="Hedgpeth")'''
newVisitor = Visits(VisitTime=Date.datetime.now(), picture="example.jpg",name="chrome")
session.add(newVisitor)
session.commit()