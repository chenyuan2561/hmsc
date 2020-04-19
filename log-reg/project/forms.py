# 导入相关信息
from flask_wtf.file import FileRequired,FileAllowed
from wtforms import Form, StringField, FileField
from wtforms.validators import Length, EqualTo, InputRequired,Regexp,Email
# 登录验证
class Log(Form):
    # validators  验证器    message   错误提示信息
    username = StringField(validators=[Length(3,10,message='用户名长度应大于3小于10')])
    password = StringField(validators=[InputRequired(message='密码必传'), Length(1, 10, message='密码长度为1~10位')])

# 注册验证
class Reg(Form):
    # EqualTo   绑定于上一个，表示保持一致
    username = StringField(validators=[Length(3,10,message='用户名长度应大于3小于10')])
    password = StringField(validators=[InputRequired(message='密码必传'), Length(1, 10, message='密码长度为1~10位')])
    check_password = StringField(validators=[Length(1, 10, message='密码长度为1~10位'), EqualTo('password', message='两次密码不一致')])
