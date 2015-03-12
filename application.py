#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    爱吃后端开发
    版本：v1
    版权：暂时归于爱聚所有
    作者：祖江，傅晓，祖山，潇飞
    时间：3/11/2015

"""

import flask
from flaskext.mysql import MySQL

application = flask.Flask(__name__)
#initialize the MySQL extension
mysql = MySQL()
application.config['MYSQL_DATABASE_USER'] = 'ajaichi'
application.config['MYSQL_DATABASE_PASSWORD'] = 'AJAiChi2015'
application.config['MYSQL_DATABASE_DB'] = 'aichi'
application.config['MYSQL_DATABASE_HOST'] = 'ajaichi.csfqe4okqais.us-east-1.rds.amazonaws.com'
mysql.init_app(application)

#obtain the cursor
cursor = mysql.connect().cursor()

#Set application.debug=true to enable tracebacks on Beanstalk log output.
#Make sure to remove this line before deploying to production.
application.debug=True




@application.route('/')
def hello_world():
    return '爱吃📱app!!<br/><br/>支持emoji 😄😄🌞 <br/><br/> by <a href="http://www.google.com ">Google</a>'






"""
    REST API Reference
    v1 indicates REST API version 1
"""

# REST API codes begin here

"""
    注册功能
"""
@application.route('/v1/register')
def register_api():
    return "Register API"


@application.route('/v1/other-register')
def other_register_api():
    return "Other register API"

@application.route('/v1/login')
def login_api():
    return "Login API"






"""
    朋友圈功能
"""



# REST API codes end here




if __name__ == '__main__':
    application.run()
#application.run(host='0.0.0.0')