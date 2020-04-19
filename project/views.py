from project import app,db
from flask import Flask,url_for,render_template,request,flash,redirect
from project.models import *



# 登录
@app.route('/login/', endpoint='login', methods=['POST','GET'])
def login():
    err = ''
    form = Log(request.form)   #初始化表单,通过request.form接收数据
    if request.method == 'POST':
        if form.validate():        #验证是否安全(数据是否合法)
            g_username = request.form.get('username')
            g_password = request.form.get('password')
            u = User.query.filter_by(username=g_username).first()
            if u:
                if g_username == u.username and int(g_password) == u.password:
                    session['name'] = g_username    # 登录成功，存入session
                    return redirect(url_for('index'))      # 重定向，返回主页
                else:
                    err = '账号或密码错误'
            else:
                err = '没有该用户'
        else:
            err = form.errors
    return render_template('login.html', err=err)

# 注册
@app.route('/register/', endpoint='register', methods=['POST','GET'])
def register():
    err = ''
    form = Reg(request.form)   #初始化表单,通过request.form接收数据
    if request.method == 'POST':
        if form.validate():        #验证是否安全(数据是否合法)
            g_username = request.form.get('username')
            g_password = request.form.get('password')
            g_check_password = request.form.get('check_password')
            u = User.query.filter_by(username=g_username).first()
            if u:
                err = '该账户已存在'
            else:
                u = User(username=g_username,password=g_password)   # 存入用户表
                db.session.add(u)
                db.session.commit()
                session['name'] = g_username       # 记录用户
                return redirect(url_for('index'))
        else:
            err = form.errors
    return render_template('register.html',err=err)




