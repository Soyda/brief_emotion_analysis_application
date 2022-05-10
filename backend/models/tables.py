from sqlalchemy import Integer, ForeignKey, String, Column, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean)
    username = Column(String)
    password = Column(String)

    notes = relationship("Notes", backref="users")

class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    date = Column(DateTime, default=datetime.date.today().strftime("%d/%m/%Y"))
    note_content = Column(String(length=300))
    note_sentiment = Column(String)