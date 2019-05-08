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
    user = None
    username = request.cookies.get("username")
    userid = request.cookies.get("userid")
    userid = int(userid)
    result1 = magen.checkUserDetention(userid)
    result2 = magen.checkUserFinance1(userid)
    print(result2,type(result2))
    return render_template("home_page.html",finance=result2,liuxiao = result1,name=username)

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
            if result != None:
                uid = str(result.id)
                res = make_response(redirect('/home_page'))
                res.set_cookie('username',result.username,expires=datetime.datetime.now()+datetime.timedelta(days=7))
                res.set_cookie('userid',uid,expires=datetime.datetime.now()+datetime.timedelta(days=7))
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

@app.route("/admin_page")
def admin_page():
    adminname = request.cookies.get("adminname")
    user = magen.querUser()
    finance = magen.checkUserFinance2()
    return render_template("admin_page.html",finance=finance,user=user,name=adminname)

# 按账号查询用户
@app.route("/admin_checkuser",methods=["POST","GET"])
def admin_checkuser():
    if request.method == "POST":
        username = request.form["username"]
        return make_response(redirect('/admin_checkuser1/'+username))

@app.route("/admin_checkuser1/<username>")
def admin_checkuser1(username):
    adminname = request.cookies.get("adminname")
    user = magen.checkUser2(username)
    return render_template("admin_checkuser.html", user=user, name=adminname)

# 按账号查询用户
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
        return render_template("admin_adduser.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.addUser(username,password,xm,gender,qq,email,address,phone)
        return make_response(redirect('/admin_adduser_success/admin_adduser'))

@app.route("/admin_adduser_success/<url>")
def admin_adduser_success(url):
    return render_template('admin_adduser_success.html',url=url)

@app.route("/admin_adduser_danger")
def admin_adduser_danger():
    return render_template('admin_adduser_danger.html')

@app.route("/admin_deleteuser/<id>")
def admin_deleteuser(id):
    print(id,'------------------')
    magen.deleteUser(id)
    return make_response(redirect('/admin_page'))

# 修改用户信息
@app.route("/admin_updateuser/<id>",methods=["GET","POST"])
def admin_updateuser(id):
    if request.method == "GET":
        result = magen.checkUser1(id)
        return render_template('admin_updateuser.html',result=result)
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        xm = request.form['xm']
        gender = request.form['gender']
        qq = request.form['qq']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']
        magen.updateuser(id,username,password,xm,gender,qq,email,address,phone)
        return make_response(redirect('/admin_page'))

# 查看用户信息
@app.route("/admin_userdetails/<id>",methods=["GET","POST"])
def admin_userdetails(id):
    result = magen.checkUser1(id)
    return render_template('admin_userdetails.html', result=result)

@app.route("/admin_addUserFinance",methods=["GET","POST"])
def admin_addUserFinance():
    if request.method == "GET":
        return render_template("admin_addUserFinance.html")
    elif request.method == "POST":
        user_xuefei = request.form["user_xuefei"]
        user_shufei = request.form["user_shufei"]
        user_zhusufei = request.form["user_zhusufei"]
        user_zhifu = request.form["user_zhifu"]
        user_sum = int(user_xuefei)+int(user_shufei)+int(user_zhusufei)
        user_qian = user_sum - int(user_zhifu)
        userid = request.form["userid"]
        # print(user_xuefei,user_shufei,userid,"&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        result = magen.addUserFinance(user_xuefei,user_shufei,user_zhusufei,user_sum,user_zhifu,user_qian,userid)
        # print(result)
        return make_response(redirect('/admin_adduser_success/admin_addUserFinance'))

@app.route("/admin_updateUserFinance/<id>",methods=["GET","POST"])
def admin_updateUserFinance(id):
    if request.method == "GET":
        result = magen.checkUserFinance3(id)
        # print(result,id,type(id),"******************************")
        return render_template("admin_updateUserFinance.html",result=result)
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

@app.route("/admin_deleteUserFinance/<id>")
def admin_deleteUserFinance(id):
    magen.deleteUserFinance(id)
    return make_response(redirect('/admin_page'))

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