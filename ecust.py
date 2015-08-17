# coding: utf-8
import urllib
import urllib2
import re
import cookielib
import os

class Ecust:
	def __init__(self):
		self.Id = ''
		self.Psw = ''
		self.Result = ''
	
	def jwc(self):
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		postdata=urllib.urlencode({
			'__EVENTTARGET': '', 
			'__EVENTARGUMENT': '', 
			'__VIEWSTATE': '/wEPDwUKLTU1MjMxMzE0NA9kFgICAQ9kFgICBg8PFgIeBFRleHQFUOWtpueUn+WIneWni+WvhueggeS4uui6q+S7veivgeWPt+WQjuWFreS9jeOAguWvhueggemVv+W6puS4jei2hei/hzEw5Liq5a2X56ym44CCZGRk5dW/RVuJXa5mTTkLLehwbkjtK7k=', 
			'TxtStudentId': self.Id, 
			'TxtPassword': self.Psw, 
			'BtnLogin': 'ç»å½', 
			'__EVENTVALIDATION': '/wEWBAK/svDDAgK/ycb4AQLVqbaRCwLi44eGDOLZGYwra2dcUhSuWLFd3bSIYQUp'
		})
		req = urllib2.Request(
			url = 'http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx', 
			data = postdata
		)
		opener.open(req)
		result = opener.open('http://202.120.108.14/ecustedu/K_StudentQuery/K_BigScoreTableDetail.aspx?key=0').read()
		unicodePage = result.decode('utf-8')
		gpa = 0
		totalscore = 0
		totalcredit = 0
		Rex = '<tr.*?>.*?<font.*?>(.*?)</font>.*?<font.*?<font.*?>(.*?)</font>.*?<font.*?<font.*?>(.*?)</font>.*?<font.*?>(.*?)</font>.*?</tr>'
		myItems = re.findall(Rex, unicodePage, re.S)
		for item in myItems:
			if item[1] == u'必修' and item[2].isdigit():
				totalscore += float(item[2])
				totalcredit += float(item[3])
				gpa += float(item[2]) * float(item[3])
		if totalcredit != 0:
			gpa /= totalcredit
			if bool == '0':
				print(u'加权平均分: %s\n' % str(gpa))
			else:
				self.Result.write('%s\t%s\t%s\n' % (self.Id, self.Psw, gpa))
		else:
			print(u'学号或密码错误\n')

print(u'''
-------------------------------
华东理工大学必修课加权平均分
操作：
输入q退出
文件读数据(默认)
手动输入请输入0
-------------------------------\n''')
print('')
my = Ecust()
bool = raw_input('文件输入or手动输入(0)：'.decode('utf-8').encode('gbk'))
print('')
if bool == 'q':
	pass
elif bool == '0':
	while True:
		q = raw_input('输入q退出:'.decode('utf-8').encode('gbk'))
		if q == 'q':
			break
		id = raw_input('\n请输入学号：'.decode('utf-8').encode('gbk'))
		print('')
		psw = raw_input('请输入密码: '.decode('utf-8').encode('gbk'))
		print(u'\n正在进行......\n')
		if id == '' or psw == '':
			print(u'学号或密码不能为空\n')
			continue
		my.Id = id
		my.Psw = psw
		my.jwc()
else:
	while True:
		q = raw_input('输入q退出:'.decode('utf-8').encode('gbk'))
		if q == 'q':
			break
		filename = raw_input('\n请输入文件名:'.decode('utf-8').encode('gbk'))
		print('')
		exist = os.path.exists(filename)
		if not exist:
			print(u'文件不存在\n')
			continue
		result = open('result.txt', "wb+")
		print(u'正在进行......\n')
		file = open(filename, 'r')
		while True:
			line = file.readline()
			if not line:
				break
			s = line.split('	')
			my.Id = s[0]
			my.Psw = s[1].replace('\n', '')
			my.Result = result
			my.jwc()
		file.close()
		result.close()