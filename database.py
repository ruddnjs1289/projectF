import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy import func
from sqlalchemy.types import DateTime


# Define the MariaDB engine using MariaDB Connector/Python

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3306/project")

Base = declarative_base()

class Visits(Base):
    __tablename__ = 'visits'

    VisitTime=sqlalchemy.Column(DateTime,primary_key=True)
    picture=sqlalchemy.Column(sqlalchemy.String(length=200))
    name=sqlalchemy.Column(sqlalchemy.String(length=50))
    
    Base.metadata.create_all(engine)
 
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

newVisitor = Visits(VisitTime=datetime.now(), picture="example.jpg",name="chrome")
session.add(newVisitor)
session.commit()