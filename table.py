import urllib
import urllib.request
from bs4 import BeautifulSoup
import string


class EPL:


	def make_soup(self, EPL):
		open_page = urllib.request.urlopen(EPL)
		soupdata = BeautifulSoup(open_page,'html.parser')
		return soupdata

	def display_table(self):
		teamdata = ''
		teampoints = ''
		i = 0
		final = []
		tot =[]
		next = []
		next_fixture = []
		soup = self.make_soup('https://www.premierleague.com/tables')
		for team in soup.findAll('tr'):
			for data in team.findAll('span', {'class': 'long'}):
				final.append(data.text)
				for point in team.findAll('td', {'class': 'points'}):
					tot.append(point.text)
			for data in team.findAll('span', {'class':'visuallyHidden'}):
				next.append(data.text)
		
		teamsort, pointsort = final[:20], tot[:20]
		
		for i in range(40):
			if i == 0 or i % 2 == 0:
				next_fixture.append(next[i])
		for i in range(0,20):
			if i <= 8:
				teamsort[i] = ' '+teamsort[i]
				formatter1 = 31 - len(teamsort[i])
				formatter = 41 - (len(teamsort[i]) + len(pointsort[i]) + formatter1)
			else:
				formatter1 = 30 - len(teamsort[i])
				formatter = 40 - (len(teamsort[i]) + len(pointsort[i]) + formatter1)
	
			
			print(int(i + 1), teamsort[i],'{}'.format(formatter1*' '), pointsort[i] , ' {} Next Fixture:'.format(formatter*' ') , next_fixture[i])
					 



	def display_home_table(self):
			teamdata = ''
			teampoints = ''
			i = 0
			final = []
			tot =[]
			next = []
			next_fixture = []
			soup = self.make_soup('https://www.premierleague.com/tables?co=1&se=210&ha=H')
			for team in soup.findAll('tr'):
				for data in team.findAll('span', {'class': 'long'}):
					final.append(data.text)
					for point in team.findAll('td', {'class': 'points'}):
						tot.append(point.text)
				for data in team.findAll('span', {'class':'visuallyHidden'}):
					next.append(data.text)
			
			teamsort, pointsort = final[:20], tot[:20]
			
			for i in range(40):
				if i == 0 or i % 2 == 0:
					next_fixture.append(next[i])
			for i in range(0,20):
				if i <= 8:
					teamsort[i] = ' '+teamsort[i]
					formatter1 = 31 - len(teamsort[i])
					formatter = 41 - (len(teamsort[i]) + len(pointsort[i]) + formatter1)
				else:
					formatter1 = 30 - len(teamsort[i])
					formatter = 40 - (len(teamsort[i]) + len(pointsort[i]) + formatter1)
		
				
				print(int(i + 1), teamsort[i],'{}'.format(formatter1*' '), pointsort[i] , ' {} Next Fixture:'.format(formatter*' ') , next_fixture[i])


	def scorers_table(self):
		player_name = []
		plays_for = []
		total_goals = []
		total_assists = []
		ordered_assists = {}
		print('Name', ' '*48, 'Team', ' '*42, 'Goals', ' '*25, 'Assists')
		site = self.make_soup('https://www.bbc.com/sport/football/premier-league/top-scorers')
		for player in site.findAll('div', {'id':'top-scorers'}):
			for name in site.findAll('h2', {'class':'top-player-stats__name gel-double-pica'}):
				player_name.append(name.text)

			for team_name in site.findAll('span',{'class': 'gel-long-primer team-short-name'}):
				plays_for.append(team_name.text)

			for tot_goals in site.findAll('span', {'class': 'top-player-stats__goals-scored-number'}):
				total_goals.append(tot_goals.text)

			for tot_assists in site.findAll('span', {'class': 'top-player-stats__assists-number gel-double-pica'}):
				total_assists.append(tot_assists.text)






		for i in range(24):
			#ordered_assists[player_name[i]] = total_assists[i]
			tabulation = 50 -len(player_name[i])
		
			if int(total_goals[i]) > 9:
				tabulation1 = 49 - len(plays_for[i])
			else:
				tabulation1 = 50 - len(plays_for[i])

			print('{}'.format(player_name[i]), ' '*tabulation, '{}'.format(plays_for[i]), ' '*tabulation1, '{}'.format(total_goals[i]), ' '*30, '{}'.format(total_assists[i]))

		#sorted_assists = sorted(ordered_assists.items(), key=lambda x: x[1])
		#print(sorted_assists)





	def upcoming_fixtures(self):
		dates = []
		full = []
		table = self.make_soup('https://www.sportytrader.com/en/results-live/football/england/premier-league-49/')
		for date in table.findAll('a', {'class':'roll-match'}):
			dates.append(''.join(date.text.split('\n')))

		dates[0].strip()


		for i in range(10):
			full.append(dates[i][44:140].strip().split('\n'))
			print(full[i][0], '\n')







	def home_record(self):
		print('Team','Played','Pts')
		stats = []
		getrecord = self.make_soup('http://1x2stats.com/en-us/ENG/Premier-League/table-home-away/')
		for teamrecord in getrecord.findAll('td'):
			stats.append(teamrecord.text)
		new = []
		for i in range(0, len(stats), 9):
			new.append(stats[i : i+9])
		for i in range(20):
			print('  '.join(new[i]))










def main():
	prem = EPL()
	print(prem.home_record())





if __name__ == '__main__':
	main()
