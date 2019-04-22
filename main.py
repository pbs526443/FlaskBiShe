from flask import Flask,render_template,request,redirect,make_response
import datetime
from orm import model
from orm import ormmanage as magen
app = Flask(__name__)
# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
# 配置debug调试错误
app.debug = True

# @app.route('/')
# def logind():
#     return redirect("/login")

# 首页界面
@app.route('/home_page')
def home_page():
    user = None
    user = request.cookies.get("username")
    userid = request.cookies.get("userid")
    userid = int(userid)
    if user:
        print("之前已经登录过")
    else:
        user = '未登录'
        print("之前没有登录过")
    result = magen.checkUserFinance(userid)
    result1 = magen.checkUserDetention(userid)
    print(result)
    print(result[0].id)
    return render_template("home_page.html",finance=result,liuxiao = result1)

# 登录界面
@app.route("/",methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = magen.checkUser(username,password)
        if result != -1:
            uid = str(result.id)
            res = make_response(redirect('/home_page'))
            res.set_cookie('username',result.username,expires=datetime.datetime.now()+datetime.timedelta(days=7))
            res.set_cookie('userid',uid,expires=datetime.datetime.now()+datetime.timedelta(days=7))
            return res
        else:
            return redirect("/login")


if __name__ == '__main__':
    app.run(host="192.168.12.168",port=8888)