from bson import json_util
import json
from flask import Flask,render_template,request,redirect,make_response
import datetime
from orm import model
from orm import ormmanage as magen
app = Flask(__name__)
# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
# 配置debug调试错误
app.debug = True


# 用户首页界面
@app.route('/home_page')
def home_page():
    username = request.cookies.get("username")
    userid = request.cookies.get("userid")
    userid = int(userid)
    result2 = magen.checkUserFinance1(userid)
    content = magen.checkContent2()
    content1 = magen.checkContent3()
    Leavingschool = magen.checkLeavingschool1(userid)
    print(result2,userid,"++++++++++++++")
    return render_template("home_page.html",finance=result2,Leavingschool = Leavingschool,name=username,content=content,content1=content1)

# 用户修改密码
@app.route("/user_updatepassword",methods=["GET","POST"])
def user_updatepassword():
    if request.method == "POST":
        id = request.cookies.get("userid")
        password = request.form["password"]
        password1 = request.form["password1"]
        if password1 == password:
            return make_response(redirect('/home_page'))
        else:
            magen.updateUserpassword(id,password1)
            return make_response(redirect('/'))

# 用户个人中心
@app.route("/user_personal",methods=["GET","POST"])
def user_personal():
    id = request.cookies.get("userid")
    if request.method == "GET":
        result = magen.checkUser1(id)
        return render_template("user_personal.html",result=result)
    elif request.method == "POST":
        xm = request.form["xm"]
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.updateuser1(id,xm,gender,qq,email,address,phone)
        return make_response(redirect('/user_personal_success'))

# 用户修改成功
@app.route("/user_personal_success")
def user_personal_success():
    return render_template("user_personal_success.html")

# 用户申请离校
@app.route("/user_addLeavingschool",methods=["POST","GET"])
def user_addLeavingschool():
    userid = request.cookies.get("userid")
    if request.method == "GET":
        return render_template("user_addLeavingschool.html")
    elif request.method == "POST":
        user_liyou = request.form['user_liyou']
        radio = 0
        magen.addLeavingschool(user_liyou,radio,userid)
        return make_response(redirect('/home_page'))

# 教师主页面
@app.route("/teacher_page")
def teacher_page():
    teachername = request.cookies.get("teachername")
    teacherid = request.cookies.get("teacherid")
    teacherid = int(teacherid)
    result = magen.checkTeacherFinance1(teacherid)
    content = magen.checkContent2()
    content1 = magen.checkContent3()
    teachercontent = magen.checkContent4(teacherid)
    Leavingschool = magen.checkLeavingschool2(teacherid)
    return render_template('teacher_page.html',Leavingschool=Leavingschool,name=teachername,finance=result,content=content,content1=content1,teachercontent=teachercontent)

# 教师修改密码
@app.route("/teacher_updatepassword",methods=["GET","POST"])
def teacher_updatepassword():
    if request.method == "POST":
        id = request.cookies.get("teacherid")
        password = request.form["password"]
        password1 = request.form["password1"]
        if password1 == password:
            return make_response(redirect('/teacher_page'))
        else:
            magen.updateTeacherpassword(id,password1)
            return make_response(redirect('/'))

# 教师修改成功
@app.route("/teacher_personal_success")
def teacher_personal_success():
    return render_template("teacher_personal_success.html")

# 教师个人中心
@app.route("/teacher_personal",methods=["GET","POST"])
def teacher_personal():
    id = request.cookies.get("teacherid")
    if request.method == "GET":
        result = magen.checkTeacher1(id)
        return render_template("teacher_personal.html",result=result)
    elif request.method == "POST":
        xm = request.form["xm"]
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.updateTeacher1(id,xm,gender,qq,email,address,phone)
        return make_response(redirect('/teacher_personal_success'))

# 教师发布公告
@app.route("/teacher_addContent",methods=["POST","GET"])
def teacher_addContent():
    id = request.cookies.get("teacherid")
    if request.method == "POST":
        content = request.form['content']
        magen.addContent(content,id)
        return make_response(redirect('/teacher_page'))

# 教师修改公告
@app.route("/teacher_updateContent/<id>",methods=["POST","GET"])
def teacher_updateContent(id):
    if request.method == "GET":
        result = magen.checkContent1(id)
        return render_template("teacher_updateContent.html",result=result)
    elif request.method == "POST":
        tid = request.cookies.get("teacherid")
        content = request.form['content']
        magen.updateContent(id,content,tid)
        return make_response(redirect('/teacher_page'))

# 教师删除公告信息
@app.route("/teacher_deleteContent/<id>")
def teacher_deleteContent(id):
    magen.deleteContent(id)
    return make_response(redirect('/teacher_page'))

# 教师审核学生留校通过
@app.route("/teacher_y_updateLeavingschool/<id>")
def teacher_y_updateLeavingschool(id):
    radio = 1
    magen.updateLeavingschoo2(id,radio)
    return make_response(redirect('/teacher_page'))

# 教师审核学生留校不通过
@app.route("/teacher_n_updateLeavingschool/<id>")
def teacher_n_updateLeavingschool(id):
    radio = 2
    magen.updateLeavingschoo2(id,radio)
    return make_response(redirect('/teacher_page'))

# 登录界面
@app.route("/",methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        radio = request.form["radio"]
        if radio == '1':
            result = magen.checkUser(username,password)
            print(result,username,password,"+++++++++++++++++")
            if result != None:
                uid = str(result.id)
                res = make_response(redirect('/home_page'))
                res.set_cookie('username',result.username,expires=datetime.datetime.now()+datetime.timedelta(days=7))
                res.set_cookie('userid',uid,expires=datetime.datetime.now()+datetime.timedelta(days=7))
                return res
            else:
                return redirect("/")
        elif radio == '2':
            result = magen.checkTeacher(username, password)
            print(result, username, password, "+++++++++++++++++")
            if result != None:
                uid = str(result.id)
                res = make_response(redirect('/teacher_page'))
                res.set_cookie('teachername', result.username,
                               expires=datetime.datetime.now() + datetime.timedelta(days=7))
                res.set_cookie('teacherid', uid, expires=datetime.datetime.now() + datetime.timedelta(days=7))
                return res
            else:
                return redirect("/")
        else:
            result = magen.checkAdmin(username,password)
            if result != None:
                aid = str(result.id)
                res = make_response(redirect('/admin_page'))
                res.set_cookie('adminname',result.username,expires=datetime.datetime.now()+datetime.timedelta(days=7))
                res.set_cookie('adminid',aid,expires=datetime.datetime.now()+datetime.timedelta(days=7))
                return res
            else:
                return redirect("/")

# admin主页面
@app.route("/admin_page")
def admin_page():
    adminname = request.cookies.get("adminname")
    user = magen.querUser()
    finance = magen.checkUserFinance2()
    teacher = magen.querTeacher()
    content = magen.checkContent()
    TeacherFinance = magen.checkTeacherFinance()
    Leavingschool = magen.querLeavingschool()
    return render_template("admin_page.html",finance=finance,TeacherFinance=TeacherFinance,Leavingschool=Leavingschool,user=user,teacher=teacher,content=content,name=adminname)

# 按账号查询用户
@app.route("/admin_checkuser",methods=["POST","GET"])
def admin_checkuser():
    if request.method == "POST":
        username = request.form["username"]
        return make_response(redirect('/admin_checkuser1/'+username))

# 按照账号查询学生
@app.route("/admin_checkuser1/<username>")
def admin_checkuser1(username):
    adminname = request.cookies.get("adminname")
    user = magen.checkUser2(username)
    return render_template("admin_checkuser.html", user=user, name=adminname)

# 按姓名查询学生财务
@app.route("/admin_checkuserfinance",methods=["POST","GET"])
def admin_checkuserfinance():
    if request.method == "POST":
        xm = request.form["xm"]
        return make_response(redirect('/admin_checkuserfinance1/' + xm))

@app.route("/admin_checkuserfinance1/<xm>")
def admin_checkuserfinance1(xm):
    adminname = request.cookies.get("adminname")
    finance = magen.checkUserFinance_xm(xm)
    return render_template("admin_checkuserfinance.html", finance=finance, name=adminname)

# 添加用户信息
@app.route("/admin_adduser",methods=["POST","GET"])
def admin_adduser():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_adduser.html",name=adminname)
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        tid = request.form['tid']
        magen.addUser(username,password,xm,gender,qq,email,address,phone,tid)
        return make_response(redirect('/admin_adduser_success/admin_adduser'))

# 添加老师信息
@app.route("/admin_addTeacher",methods=["POST","GET"])
def admin_addTeacher():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_addTeacher.html",name=adminname)
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.addTeacher(username,password,xm,gender,qq,email,address,phone)
        return make_response(redirect('/admin_adduser_success/admin_addTeacher'))

# 添加离校
@app.route("/admin_addLeavingschool",methods=["POST","GET"])
def admin_addLeavingschool():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_addLeavingschool.html",name=adminname)
    elif request.method == "POST":
        user_liyou = request.form['user_liyou']
        radio = request.form['radio']
        userid = request.form['userid']
        magen.addLeavingschool(user_liyou,radio,userid)
        return make_response(redirect('/admin_adduser_success/admin_addContent'))

# 添加公告
@app.route("/admin_addContent",methods=["POST","GET"])
def admin_addContent():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_addContent.html",name=adminname)
    elif request.method == "POST":
        content = request.form['content']
        tid = request.form['tid']
        magen.addContent(content,tid)
        return make_response(redirect('/admin_adduser_success/admin_addContent'))

# 添加教师工资
@app.route("/admin_addTeacherFinance",methods=["POST","GET"])
def admin_addTeacherFinance():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_addTeacherFinance.html",name=adminname)
    elif request.method == "POST":
        t_wages = request.form['t_wages']
        t_subsidy = request.form['t_subsidy']
        t_allowance = request.form['t_allowance']
        userid = request.form['userid']
        t_data = request.form['t_data']
        a1 = int(t_wages) + int(t_subsidy) + int(t_allowance)
        sum = int(t_wages) + int(t_subsidy) + int(t_allowance) -3500
        if sum <= 1500:
            t_tax = sum * 0.03
        elif 1500 < sum <= 4500:
            t_tax = sum * 0.1
        elif 4500 < sum <= 9000:
            t_tax = sum * 0.2
        else:
            t_tax = sum * 0.3
        t_sum = a1 - t_tax
        magen.addTeacherFinance(t_wages,t_subsidy,t_allowance,t_tax,t_sum,t_data,userid)
        return make_response(redirect('/admin_adduser_success/admin_addTeacherFinance'))

@app.route("/admin_adduser_success/<url>")
def admin_adduser_success(url):
    adminname = request.cookies.get("adminname")
    return render_template('admin_adduser_success.html',url=url,name=adminname)

@app.route("/admin_adduser_danger")
def admin_adduser_danger():
    adminname = request.cookies.get("adminname")
    return render_template('admin_adduser_danger.html',name=adminname)

# 删除学生
@app.route("/admin_deleteuser/<id>")
def admin_deleteuser(id):
    magen.deleteUser(id)
    return make_response(redirect('/admin_page'))

# 删除教师
@app.route("/admin_deleteteacher/<id>")
def admin_deleteteacher(id):
    magen.deleteTeacher(id)
    return make_response(redirect('/admin_page'))

# 删除留校
@app.route("/admin_deleteLeavingschool/<id>")
def admin_deleteLeavingschool(id):
    magen.deleteLeavingschool(id)
    return make_response(redirect('/admin_page'))

# 修改用户信息
@app.route("/admin_updateuser/<id>",methods=["GET","POST"])
def admin_updateuser(id):
    if request.method == "GET":
        result = magen.checkUser1(id)
        adminname = request.cookies.get("adminname")
        return render_template('admin_updateuser.html',result=result,name=adminname)
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        tid = request.form['tid']
        magen.updateuser(id,username,password,xm,gender,qq,email,address,phone,tid)
        return make_response(redirect('/admin_page'))

# 修改教师信息
@app.route("/admin_updateTeacher/<id>",methods=["GET","POST"])
def admin_updateTeacher(id):
    if request.method == "GET":
        result = magen.checkTeacher1(id)
        adminname = request.cookies.get("adminname")
        return render_template('admin_updateTeacher.html',result=result,name=adminname)
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.updateTeacher(id,username,password,xm,gender,qq,email,address,phone)
        return make_response(redirect('/admin_page'))

# 修改公告
@app.route("/admin_updateContent/<id>",methods=["POST","GET"])
def admin_updateContent(id):
    if request.method == "GET":
        result = magen.checkContent1(id)
        adminname = request.cookies.get("adminname")
        return render_template("admin_updateContent.html",result=result,name=adminname)
    elif request.method == "POST":
        content = request.form['content']
        tid = request.form['tid']
        magen.updateContent(id,content,tid)
        return make_response(redirect('/admin_page'))


# 修改离校
@app.route("/admin_updateLeavingschool/<id>",methods=["POST","GET"])
def admin_updateLeavingschool(id):
    if request.method == "GET":
        result = magen.checkLeavingschool(id)
        adminname = request.cookies.get("adminname")
        return render_template("admin_updateLeavingschool.html",result=result,name=adminname)
    elif request.method == "POST":
        user_liyou = request.form['user_liyou']
        radio = request.form['radio']
        userid = request.form['userid']
        print(user_liyou,id,radio,userid,"++++++++++++++++++++")
        magen.updateLeavingschool(id,user_liyou,radio,userid)
        return make_response(redirect('/admin_page'))

# 修改教师工资
@app.route("/admin_updateTeacherFinance/<id>",methods=["POST","GET"])
def admin_updateTeacherFinance(id):
    if request.method == "GET":
        result = magen.checkTeacherFinance1(id)
        adminname = request.cookies.get("adminname")
        return render_template("admin_updateTeacherFinance.html",result=result,name=adminname)
    elif request.method == "POST":
        t_wages = request.form['t_wages']
        t_subsidy = request.form['t_subsidy']
        t_allowance = request.form['t_allowance']
        userid = request.form['userid']
        t_data = request.form['t_data']
        a1 = int(t_wages) + int(t_subsidy) + int(t_allowance)
        sum = a1 - 3500
        if sum <= 1500:
            t_tax = sum * 0.03
        elif 1500 < sum <= 4500:
            t_tax = sum * 0.1
        elif 4500 < sum <= 9000:
            t_tax = sum * 0.2
        else:
            t_tax = sum * 0.3
        t_sum = a1 - t_tax
        magen.updateTeacherFinance(id,t_wages, t_subsidy, t_allowance, t_tax, t_sum, t_data, userid)
        return make_response(redirect('/admin_page'))

# 查看用户信息
@app.route("/admin_userdetails/<id>",methods=["GET","POST"])
def admin_userdetails(id):
    result = magen.checkUser1(id)
    adminname = request.cookies.get("adminname")
    return render_template('admin_userdetails.html', result=result,name=adminname)

# 查看教师信息
@app.route("/admin_Teacherdetails/<id>",methods=["GET","POST"])
def admin_Teacherdetails(id):
    result = magen.checkUser1(id)
    adminname = request.cookies.get("adminname")
    return render_template('admin_Teacherdetails.html', result=result,name=adminname)

# 查看公告信息
@app.route("/admin_Contentdetails/<id>",methods=["GET","POST"])
def admin_Contentdetails(id):
    result = magen.checkContent1(id)
    adminname = request.cookies.get("adminname")
    return render_template('admin_Contentdetails.html', result=result,nmae=adminname)


# 添加学生财务信息
@app.route("/admin_addUserFinance",methods=["GET","POST"])
def admin_addUserFinance():
    if request.method == "GET":
        adminname = request.cookies.get("adminname")
        return render_template("admin_addUserFinance.html",name=adminname)
    elif request.method == "POST":
        user_xuefei = request.form["user_xuefei"]
        user_shufei = request.form["user_shufei"]
        user_zhusufei = request.form["user_zhusufei"]
        user_zhifu = request.form["user_zhifu"]
        user_sum = int(user_xuefei)+int(user_shufei)+int(user_zhusufei)
        user_qian = user_sum - int(user_zhifu)
        userid = request.form["userid"]
        magen.addUserFinance(user_xuefei,user_shufei,user_zhusufei,user_sum,user_zhifu,user_qian,userid)
        return make_response(redirect('/admin_adduser_success/admin_addUserFinance'))

# 修改学生财务信息
@app.route("/admin_updateUserFinance/<id>",methods=["GET","POST"])
def admin_updateUserFinance(id):
    if request.method == "GET":
        result = magen.checkUserFinance3(id)
        adminname = request.cookies.get("adminname")
        return render_template("admin_updateUserFinance.html",result=result,name=adminname)
    elif request.method == "POST":
        user_xuefei = request.form["user_xuefei"]
        user_shufei = request.form["user_shufei"]
        user_zhusufei = request.form["user_zhusufei"]
        user_zhifu = request.form["user_zhifu"]
        userid = request.form["userid"]
        user_sum = int(user_xuefei) + int(user_shufei) + int(user_zhusufei)
        user_qian = user_sum - int(user_zhifu)
        magen.updateUserFinance(id,user_xuefei,user_shufei,user_zhusufei,user_sum,user_zhifu,user_qian,userid)
        return make_response(redirect('/admin_page'))

# 删除学生财务信息
@app.route("/admin_deleteUserFinance/<id>")
def admin_deleteUserFinance(id):
    magen.deleteUserFinance(id)
    return make_response(redirect('/admin_page'))

# 删除学生财务信息
@app.route("/admin_deleteTeacherFinance/<id>")
def admin_deleteTeacherFinance(id):
    magen.deleteTeacherFinance(id)
    return make_response(redirect('/admin_page'))

# 删除公告信息
@app.route("/admin_deleteContent/<id>")
def admin_deleteContent(id):
    magen.deleteContent(id)
    return make_response(redirect('/admin_page'))

# admin修改密码
@app.route("/admin_updatepassword",methods=["GET","POST"])
def admin_updatepassword():
    if request.method == "POST":
        id = request.cookies.get("adminid")
        password = request.form["password"]
        password1 = request.form["password1"]
        if password == password1:
            return make_response(redirect('/admin_page'))
        else:
            magen.updateAdminpassword(id,password1)
            return make_response(redirect('/'))

if __name__ == '__main__':
    app.run(host="192.168.12.168",port=8888)