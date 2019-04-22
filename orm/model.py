from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)

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

if __name__ == '__main__':
    Base.metadata.create_all(engine)