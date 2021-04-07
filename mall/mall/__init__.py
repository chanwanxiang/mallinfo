# 初始化pymysql为能被djangoORM模块识别的mysqlDB
from pymysql import install_as_MySQLdb

install_as_MySQLdb()
