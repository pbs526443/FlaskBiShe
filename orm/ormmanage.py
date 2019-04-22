from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session = sessionmaker()()

def checkUser(username,password):
    try:
        result= session.query(model.User).filter(model.User.username == username).filter(model.User.password==password).first()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

def checkUserFinance(userid):
    try:
        result = session.query(model.UserFinance).filter(model.UserFinance.userid == userid).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

def checkUserDetention(userid):
    try:
        result = session.query(model.UserDetention).filter(model.UserDetention.userid == userid).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()