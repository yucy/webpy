import web
import settings

class hello(object):
	def GET(self):
		data={'name':'admin','passwd':'admin123'}
		return settings.render.test(data)
