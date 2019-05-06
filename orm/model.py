from sqlalchemy import create_engine
from bson import ObjectId
import pymongo
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean

class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)
    xm = Column(String(20),nullable=True)
    gender = Column(Integer,nullable=False)
    qq = Column(String(20),nullable=True)
    email = Column(String(20),nullable=True)
    address = Column(String(100),nullable=True)
    phone = Column(String(30),nullable=True)



class UserFinance(Base):
    __tablename__ = "userfinance"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    user_xuefei = Column(String(20),nullable=False)
    user_shufei = Column(String(20),nullable=False)
    # user_yijiao = Column(String(20), nullable=False)
    # user_weijiao = Column(String(20), nullable=False)
    # user_shenyu = Column(String(20), nullable=False)
    userid = Column(Integer,ForeignKey("user.id"),nullable=False)

class UserDetention(Base):
    __tablename__ = "userdetention"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    user_name = Column(String(20),nullable=False)
    user_liyou = Column(String(200),nullable=False)
    user_ztai = Column(Boolean,nullable=False)
    userid = Column(Integer,ForeignKey("user.id"),nullable=False)

con = pymongo.MongoClient()
db1 = con["admin"].authenticate("root","123456")
db = con["bishe"]
collection = db["UserFinance"]

class fjson:
    def __init__(self,userid=0,username=0,password=0,xm=None,gender=None,qq=None,email=None,address=None,phone=None,_id=None,user_xuefei=0,user_shufei=0):
        self.f1 = {"userid":userid}
        self.f2 = {"username":username,"password":password,"xm":xm,"gender":gender,"qq":qq,"email":email,
                   "address":address,"phone":phone}
        self.f3 = {"user_xuefei":user_xuefei,"user_shufei":user_shufei,"userid":int(userid)}
        self.f4 = {"_id": ObjectId(_id)}
        self.f5 = {"_id": ObjectId(_id), "user_xuefei": user_xuefei, "user_shufei": user_shufei, "userid": int(userid)}
        self.f6 = {"password":password}
        self.f7 = {"xm": xm, "gender": gender, "qq": qq, "email": email,"address": address, "phone": phone}


if __name__ == '__main__':
    Base.metadata.create_all(engine)