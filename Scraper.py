import urllib, csv, xlwt
from bs4 import BeautifulSoup

def premier_league_table():

	url = "https://www.premierleague.com/tables"

	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')

	#finds all rows for premier league
	trs = soup.findAll('tr', { "data-compseason" : "54"})

	#this will store a dictionary with weekly stats for each team
	table_data = []

	for element in trs:

		team = []
		name = element['data-filtered-table-row-name']

		#finds the rank for each team
		x = element.findAll('span', {'class' : 'value'})[0]
		pos = x.contents[0]

		#gathers table data/stats for each team
		cells = element.findAll('td')

		#table-data/stats
		team.append(int(pos))
		team.append(str(name))
		for x in range(3, 11):
			team.append(int(cells[x].contents[0]))

		table_data.append(team)

	return table_data

def data_to_xl(table_data):

	fieldnames = ['Rank', 'Club', 'Played', 'Won', 'Drawn', 'Lost'
	,'GF', 'GA', 'GD', 'Points']

	# with open('premier_league.csv', 'wb') as file:

	# 	writer = csv.writer(file)
	# 	for row in table_data:
			# writer.writerow(row)

	wb = xlwt.Workbook()
	ws = wb.add_sheet('Week1')

	for x in range(0, len(fieldnames)):
		ws.write(0, x, fieldnames[x])

	wb.save('premier_league.xls')


data_to_xl(premier_league_table())
