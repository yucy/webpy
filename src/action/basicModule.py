#coding=utf-8
from src.action.base import base
import pdb

# 主页（登陆页）
class index(base):
	def GET(self):
		return self.render('login')

# 登陆		
class login(base):
	
	def GET(self):
		return self.render('login')

	def POST(self):
		#pdb.set_trace() # 开启debug调试
		data={'name':'admin','passwd':'admin123'}
		self.assign('testData','aaa')
		res = list(self.db.query("SELECT name,passwd  FROM `my_user` "))
		self.assign('data',res)
		return self.render('test')


