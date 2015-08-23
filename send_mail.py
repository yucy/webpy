# coding:UTF-8
'''
发送txt文本邮件
'''
import smtplib
from email.mime.text import MIMEText
mailto_list=['cy.yu@139.com']
# 发送者信息
mail_host='smtp.163.com' # 邮件服务器
mail_user='yuconyu' # 用户名
mail_pass= 'fzfspybbqqxmfllq'# 'test123456' # 口令
mail_postfix='163.com' # 发件箱的后缀

def send_mail(to_list,sub,content):
	me = 'test'+'<'+mail_user+'@'+mail_postfix+'>'
	msg = MIMEText(content,_subtype='plain',_charset='gb2312')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ';'.join(to_list)
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user,mail_pass)
		server.sendmail(me,to_list,msg.as_string())
		server.close()
		return True
	except Exception,e:
		print str(e)

if __name__ == '__main__':
	# 邮件标题
	title = u'邮件测试'
	# 邮件内容
	content = u'你好，这是一封测试邮件。'
	if send_mail(mailto_list,title ,content):
		print '发送成功'
	else:
		print '发送失败'
