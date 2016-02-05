from lxml import html
import requests

page = requests.get('https://police.wustl.edu/Pages/Daily-Crime-Log-Archive.aspx')
tree = html.fromstring(page.content)
#This will create a list of months
dates = tree.xpath('//span[@class="month"]/text()')
#This will create a list of days
days = tree.xpath('//span[@class="day"]/text()')
#This will create a list of times
times = tree.xpath('//li[@class="time"]/text()')
#This will create a list of types [of crime]
types = tree.xpath('//li[@class="type"]/text()')
#This will create a list of locations
locations = tree.xpath('//li[@class="loc"]/text()')
#This will create a list of details
details = tree.xpath('//div[@class="alert"]//div[@class="details"]/text()')
#This will create a list of report numbers, occurred (time), synopses, disposition
reportNumbers, occurred, synopses, disposition = [], [], [], []
for i in range(len(details)):
	if i%4==0:
		reportNumbers.append(details[i])
	elif i%4==1:
		occurred.append(details[i])
	elif i%4==2:
		synopses.append(details[i])
	elif i%4==3:
		disposition.append(details[i])

print 'Dates: ', dates
print 'Days: ', days
print 'Times: ', times
print 'Types: ', types
print 'Locations: ', locations
print 'Report Number: ', reportNumbers
print 'Time Occurred: ', occurred
print 'Synopses: ', synopses
print 'Disposition: ', disposition
