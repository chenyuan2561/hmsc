from project import db

class User(db.Model):
    """ 用户表 """
    __tablename__ = 't_user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(22),unique=True) # 用户名（账户），不可更改
    password = db.Column(db.Integer)    # 密码