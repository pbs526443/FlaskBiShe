from sqlalchemy import create_engine
from bson import ObjectId,json_util
import pymongo,json
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
    tid = Column(Integer, ForeignKey("teacher.id"), nullable=False)

class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)
    xm = Column(String(20),nullable=True)
    gender = Column(Integer,nullable=False)
    qq = Column(String(20),nullable=True)
    email = Column(String(20),nullable=True)
    address = Column(String(100),nullable=True)
    phone = Column(String(30),nullable=True)

class Leavingschool(Base):
    __tablename__ = "Leavingschool"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    user_name = Column(String(20),nullable=False)
    user_liyou = Column(String(200),nullable=False)
    user_ztai = Column(Integer,nullable=False)
    uid = Column(Integer,ForeignKey("user.id"),nullable=False)
    tid = Column(Integer,nullable=False)

con = pymongo.MongoClient()
db1 = con["admin"].authenticate("root","123456")
db = con["bishe"]
collection = db["UserFinance"]
content = db["Content"]
collection1 = db["TeacherFinance"]
class fjson:
    def __init__(self,userid=0,username=0,password=0,xm=None,gender=None,qq=None,email=None,address=None,phone=None,
                 _id=None,user_xuefei=0,user_shufei=0,user_zhusufei=0,user_sum=0,user_zhifu=0,user_qian=0,content=0,
                 t_wages=0,t_subsidy=0,t_allowance=0,t_tax=0,t_sum=0,t_data=0,user_liyou=0,tid =0):
        self.f1 = json.dumps({"userid":int(userid)})
        self.f2 = json.dumps({"username":username,"password":password,"xm":xm,"gender":gender,"qq":qq,"email":email,
                   "address":address,"phone":phone,"tid":int(userid)})
        self.f3 = json.dumps({"user_xuefei":user_xuefei,"user_shufei":user_shufei,"user_zhusufei":user_zhusufei,
                   "user_sum":user_sum,"user_zhifu":user_zhifu,"user_qian":user_qian,"userid":int(userid),"xm":xm})
        self.f4 = json_util.dumps({"_id": ObjectId(_id)})
        self.f5 = json.dumps({"user_name":xm,"user_liyou":user_liyou,"user_ztai":gender,"uid":int(userid),"tid":tid})
        self.f51 = json.dumps({"user_ztai":gender})
        self.f6 = json.dumps({"password":password})
        self.f7 = json.dumps({"xm": xm, "gender": gender,"qq": qq,"email": email,"address": address,"phone": phone})
        self.f8 = json.dumps({"xm":xm})
        self.f9 = json.dumps({"content":content,"tid":int(userid),"xm":xm})
        self.f10 = json.dumps({"tid":int(userid)})
        self.f11 = json.dumps({"t_wages":t_wages,"t_subsidy":t_subsidy,"t_allowance":t_allowance,"t_tax":t_tax,"t_sum":t_sum,"t_data":t_data,"tid":int(userid),"xm":xm})


if __name__ == '__main__':
    Base.metadata.create_all(engine)