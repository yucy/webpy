#coding=utf-8
import web
from src.urls.myurls import urls
from settings import *

if __name__ == "__main__":
    app = web.application(urls,globals())
    web.config.debug = debug
    web.config.session_parameters['cookie+name'] = 'yy_test'
    web.config.session_parameters['cookie_domain'] = None
    web.config.session_parameters['timeout'] = yy_cookie['save_cookie_seconds']
    web.config.session_parameters['ignore_change_ip'] = True
    web.config.session_parameters['secret_key'] = yy_cookie['secret_key']
    web.config.session_parameters['expired_message'] = 'hah , this session expired ^_^'
    session = web.session.Session(app , web.session.DiskStore('data/sessions'),initializer={'login':False})
    def session_hook():
    	web.ctx.session = session
    app.add_processor(web.loadhook(session_hook))
    app.run()
