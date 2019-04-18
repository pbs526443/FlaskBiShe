from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)
from sqlalchemy import Column,Integer,String,ForeignKey
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(20),nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)