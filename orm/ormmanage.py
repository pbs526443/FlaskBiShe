from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)
import pymongo,json
from sqlalchemy.orm import sessionmaker
session = sessionmaker()()

def checkAdmin(username,password):
    try:
        result= session.query(model.Admin).filter(model.Admin.username == username).filter(model.Admin.password==password).first()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

def querUser():
    try:
        result = session.query(model.User).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()


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

def checkUser1(id):
    try:
        result= session.query(model.User).filter(model.User.id == id).first()
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

# 查询个人财务信息
def checkUserFinance1(userid):
    try:
        # print(model.fjson().f1(userid=userid),"_____________________")
        # f1 = {'userid':userid}
        result = model.collection.find(model.fjson(userid).f1)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询所有财务信息
def checkUserFinance2():
    try:
        result = model.collection.find()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询单个财务信息
def checkUserFinance3(_id):
    try:
        result = model.collection.find_one(model.fjson(_id=_id).f4)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 留校查询
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

def addUser(username,password,xm,gender,qq,email,address,phone):
    try:
        session.add(model.User(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone))
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

# 添加财务信息
def addUserFinance(user_xuefei,user_shufei,userid):
    try:
        model.collection.insert(model.fjson(user_xuefei=user_xuefei,user_shufei=user_shufei,userid=userid).f3)
    except Exception as e:
        print(e)

# 删除用户
def deleteUser(userid):
    try:
        session.query(model.User).filter(model.User.id == userid).delete()
        session.commit()
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

# 删除单个财务信息
def deleteUserFinance(_id):
    try:
        model.collection.delete_one(model.fjson(_id=_id).f4)
    except Exception as e:
        print(e)

# 修改用户信息
def updateuser(id,username,password,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(model.fjson(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f2)
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 用户修改个人信息
def updateuser1(id,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(model.fjson(xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f7)
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改管理员密码
def updateAdminpassword(id,password):
    try:
        result = session.query(model.Admin).filter(model.Admin.id == id).update(
            model.fjson(password=password).f6)
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改用户密码
def updateUserpassword(id,password):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(
            model.fjson(password=password).f6)
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改财务信息
def updateUserFinance(_id,user_xuefei,user_shufei,userid):
    try:
        model.collection.update_one(model.fjson(_id=_id).f4,{'$set':model.fjson(_id=_id,user_xuefei=user_xuefei,user_shufei=user_shufei,userid=userid).f5})
    except Exception as e:
        print(e)