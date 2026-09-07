from sqlalchemy import Column,Integer,Text, ForeignKey,String
# from sqlalchemy import PrimaryKeyConstraint
from db import Base

class User(Base):
    __tablename__= "users" 
    id = Column(Integer,primary_key= True,index = True)
    email_id = Column(String(100),unique = True,nullable=False)
    password = Column(String(10))
class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer,primary_key= True,index = True)
    u_id = Column(Integer,ForeignKey("users.id"))
    resuma_text = Column(Text)
    result = Column(Text)
    # resuma_text = Column(Text)
    # goal = Column(String(255))   # ✅ add this column
    # skills = Column(Text)
    # missing_skills = Column(Text)
    # roadmap = Column(Text)
    # interview_questions = Column(Text)
