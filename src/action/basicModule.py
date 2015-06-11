#coding=utf-8
from src.action.base import base
import time
from settings import *
import pdb,traceback

# 主页（登陆页）
class index(base):
	def GET(self):
		# 把用户名密码默认填好
		self.assign({'name':'admin','passwd':'admin123'})
		return self.render('login')

# 登陆		
class login(base):
	
	def GET(self):
		# 把用户名密码默认填好
		self.assign({'name':'admin','passwd':'admin123'})
		return self.render('login')

	def POST(self,_=''):
		pdb.set_trace() # 开启debug调试
		post = web.input()
		name = self.htmlSpecialChar(post['username'])
		passwd = post['passwd']
		res = self.db.query("SELECT name,passwd  FROM `my_user` where name = $u",vars={
			'u':name
			})
		try:
			user = res[0]
			if passwd != user['passwd']:
				return self.showJson({
					'num':1,
					'msg':u'账号密码错误'
					})
			else:
				lasttime  = int(time.time())
				web.ctx.session.login = True
				web.ctx.session.lasttime = lasttime
				web.ctx.session.uname=user['name']
				return self.render('center')
		except Exception,e:
			print traceback.print_exc()
			return self.showJson({
				'num':3,
				'msg':u'EXCEPTION:'+str(e.args)
				})
		


