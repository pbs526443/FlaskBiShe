from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/bishedb",
                                    encoding='utf8', echo=True)
import pymongo,json
from bson import json_util
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

# 查询所有离校信息
def querLeavingschool():
    try:
        result = session.query(model.Leavingschool).all()
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

# 根据账号查询学生
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
        result = model.collection.find(json.loads(model.fjson(userid).f1))
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
        result = model.content.find_one(json_util.loads(model.fjson(_id=_id).f4))
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
        result = model.content.find(json.loads(model.fjson(userid=id).f10)).sort([("_id",pymongo.DESCENDING)])
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 根据id查询离校
def checkLeavingschool(id):
    try:
        result= session.query(model.Leavingschool).filter(model.Leavingschool.id == id).first()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

# 用户查询自己的所有离校
def checkLeavingschool1(id):
    try:
        result= session.query(model.Leavingschool).filter(model.Leavingschool.uid == id).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

# 教师查询自己的学生的所有离校
def checkLeavingschool2(id):
    try:
        result= session.query(model.Leavingschool).filter(model.Leavingschool.tid == id).all()
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        session.close()

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
        result = model.collection.find_one(json_util.loads(model.fjson(_id=_id).f4))
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
        result = model.collection1.find_one(json_util.loads(model.fjson(_id=id).f4))
        if result:
            return result
        else:
            return None
    except Exception as e:
        print(e)

# 添加用户
def addUser(username,password,xm,gender,qq,email,address,phone,tid):
    try:
        session.add(model.User(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone,tid=tid))
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
        model.collection.insert(json.loads(model.fjson(user_xuefei=user_xuefei,user_shufei=user_shufei,user_zhusufei=user_zhusufei,user_sum=user_sum,user_zhifu=user_zhifu,user_qian=user_qian,userid=userid,xm=xm).f3))
    except Exception as e:
        print(e)

# 添加教师财务信息
def addTeacherFinance(t_wages,t_subsidy,t_allowance,t_tax,t_sum,t_data,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.collection1.insert(json.loads(model.fjson(t_wages=t_wages,t_subsidy=t_subsidy,t_allowance=t_allowance,t_tax=t_tax,t_sum=t_sum,t_data=t_data,userid=userid,xm=xm).f11))
    except Exception as e:
        print(e)

# 添加公告
def addContent(content,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.content.insert(json.loads(model.fjson(content=content,userid=userid, xm=xm).f9))
    except Exception as e:
        print(e)

# 添加离校模申请
def addLeavingschool(user_liyou,radio,userid):
    try:
        xm = checkUser1(userid).xm
        tid = checkUser1(userid).tid
        session.add(model.Leavingschool(user_name=xm, user_liyou=user_liyou,user_ztai=radio,uid=userid,tid=tid))
        session.commit()
    except Exception as e:
        print(e)

# 删除学生
def deleteUser(userid):
    try:
        session.query(model.User).filter(model.User.id == userid).delete()
        session.commit()
        model.collection.delete_many(json.dumps(model.fjson(userid=userid).f1))
    except Exception as e:
        print(e)
    finally:
        session.close()

# 删除教师
def deleteTeacher(userid):
    try:
        session.query(model.Teacher).filter(model.Teacher.id == userid).delete()
        session.commit()
        model.content.delete_many(json.loads(model.fjson(userid=userid).f10))
        model.collection1.delete_many(json.loads(model.fjson(userid=userid).f10))
    except Exception as e:
        print(e)
    finally:
        session.close()

# 删除留校信息
def deleteLeavingschool(uid):
    try:
        session.query(model.Leavingschool).filter(model.Leavingschool.id == uid).delete()
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()


# 删除单个学生财务信息
def deleteUserFinance(_id):
    try:
        model.collection.delete_one(json_util.loads(model.fjson(_id=_id).f4))
    except Exception as e:
        print(e)

# 删除单个教师工资信息
def deleteTeacherFinance(_id):
    try:
        model.collection1.delete_one(json_util.loads(model.fjson(_id=_id).f4))
    except Exception as e:
        print(e)

# 删除单个公告信息
def deleteContent(_id):
    try:
        model.content.delete_one(json_util.loads(model.fjson(_id=_id).f4))
    except Exception as e:
        print(e)

# 修改学生信息
def updateuser(id,username,password,xm,gender,qq,email,address,phone,tid):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(json.loads(model.fjson(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone,userid=tid).f2))
        session.commit()
        model.collection.update_many(json.dumps(model.fjson(userid=id).f1), {'$set': json.loads(model.fjson(xm=xm).f8)})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改教师信息
def updateTeacher(id,username,password,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.id == id).update(json.loads(model.fjson(username=username,password=password,xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f2))
        session.commit()
        model.collection1.update_many(json.loads(model.fjson(userid=id).f10), {'$set': json.loads(model.fjson(xm=xm).f8)})
        model.content.update_many(json.loads(model.fjson(userid=id).f10), {'$set': json.loads(model.fjson(xm=xm).f8)})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 用户修改个人信息
def updateuser1(id,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.User).filter(model.User.id == id).update(json.loads(model.fjson(xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f7))
        session.commit()
        model.collection.update_many(json.dumps(model.fjson(userid=id).f1),{'$set':json.loads(model.fjson(xm=xm).f8)})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改用户离校信息
def updateLeavingschool(id,user_liyou,radio,userid):
    try:
        xm = checkUser1(userid).xm
        tid = checkUser1(userid).tid
        result = session.query(model.Leavingschool).filter(model.Leavingschool.id == id).update(json.loads(model.fjson(xm=xm,user_liyou=user_liyou,gender=radio,userid=userid,tid=tid).f5))
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 教师修改学生离校信息
def updateLeavingschoo2(id,radio):
    try:
        result = session.query(model.Leavingschool).filter(model.Leavingschool.id == id).update(json.loads(model.fjson(gender=radio).f51))
        session.commit()
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 教师修改个人信息
def updateTeacher1(id,xm,gender,qq,email,address,phone):
    try:
        result = session.query(model.Teacher).filter(model.Teacher.id == id).update(json.loads(model.fjson(xm=xm,gender=gender,qq=qq,email=email,address=address,phone=phone).f7))
        session.commit()
        model.collection1.update_many(json.loads(model.fjson(userid=id).f10),{'$set':json.loads(model.fjson(xm=xm).f8)})
        model.content.update_many(json.loads(model.fjson(userid=id).f10), {'$set': json.loads(model.fjson(xm=xm).f8)})
        return result
    except Exception as e:
        print(e)
    finally:
        session.close()

# 修改管理员密码
def updateAdminpassword(id,password):
    try:
        result = session.query(model.Admin).filter(model.Admin.id == id).update(
            json.loads(model.fjson(password=password).f6))
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
            json.loads( model.fjson(password=password).f6))
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
            json.loads(model.fjson(password=password).f6))
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
        model.collection.update_one(json_util.loads(model.fjson(_id=_id).f4),
                                    {'$set':json.loads(model.fjson(user_xuefei=user_xuefei,user_shufei=user_shufei,user_zhusufei=user_zhusufei,user_sum=user_sum,user_zhifu=user_zhifu,user_qian=user_qian,userid=userid,xm=xm).f3)})
    except Exception as e:
        print(e)

# 修改教师财务信息
def updateTeacherFinance(_id,t_wages,t_subsidy,t_allowance,t_tax,t_sum,t_data,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.collection1.update_one(json_util.loads(model.fjson(_id=_id).f4),
                                    {'$set':json.loads(model.fjson(t_wages=t_wages,t_subsidy=t_subsidy,t_allowance=t_allowance,t_tax=t_tax,t_sum=t_sum,t_data=t_data,userid=userid,xm=xm).f11)})
    except Exception as e:
        print(e)


# 修改公告信息
def updateContent(_id,content,userid):
    try:
        xm = checkTeacher1(userid).xm
        model.content.update_one(json_util.loads(model.fjson(_id=_id).f4),
                                    {'$set':json.loads(model.fjson(content=content,userid=userid, xm=xm).f9)})
    except Exception as e:
        print(e)