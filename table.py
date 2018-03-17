import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
import texttable as tt

headings = ['Team','Pts']
tab.header(headings)


def make_soup(EPL):
	open_page = urllib.request.urlopen(EPL)
	soupdata = BeautifulSoup(open_page,'html.parser')
	return soupdata

def teamname():
	teamdata = ''
	teampoints = ''
	i = 0
	final = []
	tot =[]

	soup = make_soup('https://www.premierleague.com/tables')
	for team in soup.findAll('tr'):
		for data in team.findAll('span', {'class': 'long'}):
			final.append(data.text)
			for point in team.findAll('td', {'class': 'points'}):
				tot.append(point.text)
	
	teamsort, pointsort = final[:20], tot[:20]
	for i in range(0,20):
		print(int(i + 1), teamsort[i], pointsort[i])
				 

teamname()

