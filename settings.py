#coding=utf-8
import web

# 链接数据库
database = 'db/my.s3db'
db = web.database(dbn = 'sqlite',db = database)

# 网址为空时自动获取
root_site = ''

#cookie设定
yy_cookie = {
	'save_cookie_seconds':86400,
	'secret_key':'yy'
}

# debug模式
debug = True