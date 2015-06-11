#coding=utf-8
import random, json, string
from hashlib import md5
from settings import *


class base:
	def __init__(self):
		self.db = db #数据库
		self.tplData = {}
		self.globalTplFunc = {}
		self.initCommonTplFunc()
		# 网站根目录
		if "" == root_site:
			self.root_site = "%s://%s/" % (web.ctx.protocol,web.ctx.host)
		else:
			self.root_site = root_site
		self.assign('root',self.root_site)
		self.assign('static',self.root_site+'static')

	# 公共模板函数
	def initCommonTplFunc(self):
		substr = lambda strings,offset,length : self.subText(strings,offset,length)
		self.assignTplFunc({'subStr':substr})

	# 自定义模板函数
	def assignTplFunc(self,funcs):
		self.globalTplFunc = dict(self.globalTplFunc,**funcs)

	# 判断是否登录
	def isLogin(self):
		return hasattr(web.ctx.session,'login') and web.ctx.session.login == True

	# MD5加密
	def md5(sef,str):
		m = md5()
		m.update(str)
		return m.hexdigest()

	# 字符转义，避免XSS攻击和SQL注入
	def safeChar(self,txt):
		return txt.replace('<','').replace('>','')\
			.replace('&','').replace('"','').replace("'","")

	# html特殊字符转义
	def htmlSpecialChar(self,txt):
		return txt.replace('<','&lt;').replace('>','&gt;')\
			.replace('"','&quot;').replace("'","&#039;")

	# 返回一个随机字符串
	def randStr(self,len=8):
		return ''.join(random.sample(string.ascii_letters+string.digits,len))

	# 截取字符串
	def subText(self,strings,offset,length):
		return self.trip_tags(strings)[offset:length]

	#
	def strip_tags(self,html):
		from HTMLParser import HTMLParser
		html = html.strip()
		html = html.strip("\n")
		result = []
		parse = HTMLParser()
		parse.handle_date = result.append
		parse.feed(html)
		parse.close()
		return ''.join(result)

	# 返回json字符串
	def  showJson(self,data):
		j = json.dumps(data)
		return j

	# 自定义模板数据
	def assign(self,key,value=''):
		# 如果key是个字典集合，则合并
		if type(key) == dict:
			# 字典合并，这样写相当于：temp = self.tplData.copy() temp.update(key)
			self.tplData = dict(self.tplData,**key) 
		else:
			self.tplData[key] = value

	# 渲染页面(后台)
	def render(self,tplName):
		self.tplData['render'] = web.template.render('view',globals=self.globalTplFunc)
		return getattr(self.tplData['render'],tplName)(self.tplData)
