# coding: utf-8
import urllib
import urllib2
import re
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({
	'__EVENTTARGET': '', 
	'__EVENTARGUMENT': '', 
	'__VIEWSTATE': '/wEPDwUJMTg2MzE1NTYyD2QWAgIBD2QWAgIGDw8WAh4EVGV4dAVQ5a2m55Sf5Yid5aeL5a+G56CB5Li66Lqr5Lu96K+B5Y+35ZCO5YWt5L2N44CC5a+G56CB6ZW/5bqm5LiN6LaF6L+HMTDkuKrlrZfnrKbjgIJkZGTItFe6UDnNqdE2sz592HXKwZ7Fhw==', 
	'TxtStudentId': '', 
	'TxtPassword': '', 
	'BtnLogin': 'ç»å½', 
	'__EVENTVALIDATION': '/wEWBALplYnsCgK/ycb4AQLVqbaRCwLi44eGDNL1/UVfta6zTJ9DMRXMNe6Ao6Wm'
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
	print(u'加权平均分: %s\n' % str(gpa))
else:
	print(u'学号或密码错误\n')
