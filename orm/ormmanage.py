from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)
import pymongo,json
import re
from sqlalchemy.orm import sessionmaker
session = sessionmaker()()

# 管理员登录
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

# 查询所有学生
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

# 查询所有教师
def querTeacher():
    try:
        result = session.query(model.Teacher).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

# 学生登录
def checkUser(username,password):
    try:
        result = session.query(model.User).filter(model.User.username == username).filter(model.User.password == password).first()
        print(result)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

# 教师登录
def checkTeacher(username,password):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.username == username).filter(model.Teacher.password == password).first()
        print(result)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()


# 根据id查询学生
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

# 根据id查询教师
def checkTeacher1(id):
    try:
        result= session.query(model.Teacher).filter(model.Teacher.id == id).first()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

def checkUser2(username):
    try:
        username = '%' + username + '%'
        result= session.query(model.User).filter(model.User.username.like(username)).all()
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
        result = model.collection.find(model.fjson(userid).f1)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 根据xm查找信息
def checkUserFinance_xm(xm):
    try:
        result = model.collection.find({'xm':re.compile(xm)})
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)


# 查询所有公告信息
def checkContent():
    try:
        result = model.content.find()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询单个公告信息
def checkContent1(_id):
    try:
        result = model.content.find_one(model.fjson(_id=_id).f4)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询最新公告信息
def checkContent2():
    try:
        result = model.content.find().limit(1).sort([("_id",pymongo.DESCENDING)])
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询最新三个公告信息
def checkContent3():
    try:
        result = model.content.find().limit(3).sort([("_id",pymongo.DESCENDING)])
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询教师所有的公告信息
def checkContent4(id):
    try:
        result = model.content.find(model.fjson(userid=id).f10).sort([("_id",pymongo.DESCENDING)])
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询所有学生财务信息
def checkUserFinance2():
    try:
        result = model.collection.find()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询单个学生财务信息
def checkUserFinance3(_id):
    try:
        result = model.collection.find_one(model.fjson(_id=_id).f4)
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询所有教师财务信息
def checkTeacherFinance():
    try:
        result = model.collection1.find()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 查询单个教师工资信息
def checkTeacherFinance1(id):
    try:
        result = model.collection1.find(model.fjson(userid=id).f10)
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

# 添加用户
def addUser(username,password,xm,gender,qq,email,address,phone):
    try:
        session.add(model.User(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone))
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

# 添加教师
def addTeacher(username,password,xm,gender,qq,email,address,phone):
    try:
        session.add(model.Teacher(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone))
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

# 添加学生财务信息
def addUserFinance(user_xuefei,user_shufei,user_zhusufei,user_sum,user_zhifu,user_qian,userid):
    try:
        xm = checkUser1(userid).xm
        model.collection.insert(model.fjson(user_xuefei=user_xuefei,user_shufei=user_shufei,user_zhusufei=user_zhusufei,user_sum=user_sum,user_zhifu=user_zhifu,user_qian=user_qian,userid=userid,xm=xm).f3)
    except Exception as e:
        print(e)

# 添加教师财务信息
def addTeacherFinance(t_wages,t_subsidy,t_allowance,t_tax,t_sum,t_data,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.collection1.insert(model.fjson(t_wages=t_wages,t_subsidy=t_subsidy,t_allowance=t_allowance,t_tax=t_tax,t_sum=t_sum,t_data=t_data,userid=userid,xm=xm).f11)
    except Exception as e:
        print(e)

# 添加公告模块
def addContent(content,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.content.insert(model.fjson(content=content,userid=userid, xm=xm).f9)
    except Exception as e:
        print(e)

# 删除学生
def deleteUser(userid):
    try:
        session.query(model.User).filter(model.User.id == userid).delete()
        session.commit()
        model.collection.delete_many(model.fjson(userid=userid).f1)
    except Exception as e:
        print(e)
    finally:
        session.close()

# 删除教师
def deleteTeacher(userid):
    try:
        session.query(model.Teacher).filter(model.Teacher.id == userid).delete()
        session.commit()
        model.content.delete_many(model.fjson(userid=userid).f10)
        model.collection1.delete_many(model.fjson(userid=userid).f10)
    except Exception as e:
        print(e)
    finally:
        session.close()

# 删除单个学生财务信息
def deleteUserFinance(_id):
    try:
        model.collection.delete_one(model.fjson(_id=_id).f4)
    except Exception as e:
        print(e)

# 删除单个教师工资信息
def deleteTeacherFinance(_id):
    try:
        model.collection1.delete_one(model.fjson(_id=_id).f4)
    except Exception as e:
        print(e)

# 删除单个公告信息
def deleteContent(_id):
    try:
        model.content.delete_one(model.fjson(_id=_id).f4)
    except Exception as e:
        print(e)

# 修改学生信息
def updateuser(id,username,password,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(model.fjson(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f2)
        session.commit()
        model.collection.update_many(model.fjson(userid=id).f1, {'$set': model.fjson(xm=xm).f8})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改教师信息
def updateTeacher(id,username,password,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.id == id).update(model.fjson(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f2)
        session.commit()
        model.collection1.update_many(model.fjson(userid=id).f10, {'$set': model.fjson(xm=xm).f8})
        model.content.update_many(model.fjson(userid=id).f10, {'$set': model.fjson(xm=xm).f8})
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
        model.collection.update_many(model.fjson(userid=id).f1,{'$set':model.fjson(xm=xm).f8})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 教师修改个人信息
def updateTeacher1(id,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.id == id).update(model.fjson(xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f7)
        session.commit()
        model.collection1.update_many(model.fjson(userid=id).f10,{'$set':model.fjson(xm=xm).f8})
        model.content.update_many(model.fjson(userid=id).f10, {'$set': model.fjson(xm=xm).f8})
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

# 修改教师密码
def updateTeacherpassword(id,password):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.id == id).update(
            model.fjson(password=password).f6)
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改学生财务信息
def updateUserFinance(_id,user_xuefei,user_shufei,user_zhusufei,user_sum,user_zhifu,user_qian,userid):
    try:
        xm = checkUser1(userid).xm
        model.collection.update_one(model.fjson(_id=_id).f4,
                                    {'$set':model.fjson(user_xuefei=user_xuefei,user_shufei=user_shufei,user_zhusufei=user_zhusufei,user_sum=user_sum,user_zhifu=user_zhifu,user_qian=user_qian,userid=userid,xm=xm).f3})
    except Exception as e:
        print(e)

# 修改教师财务信息
def updateTeacherFinance(_id,t_wages,t_subsidy,t_allowance,t_tax,t_sum,t_data,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.collection1.update_one(model.fjson(_id=_id).f4,
                                    {'$set':model.fjson(t_wages=t_wages,t_subsidy=t_subsidy,t_allowance=t_allowance,t_tax=t_tax,t_sum=t_sum,t_data=t_data,userid=userid,xm=xm).f11})
    except Exception as e:
        print(e)


# 修改公告信息
def updateContent(_id,content,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.content.update_one(model.fjson(_id=_id).f4,
                                    {'$set':model.fjson(content=content,userid=userid, xm=xm).f9})
    except Exception as e:
        print(e)