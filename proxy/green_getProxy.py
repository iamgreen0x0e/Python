import urllib2
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
def readContent(url):
	response = urllib2.urlopen(url)
	try:
		return response.read()
	except:
		return False



def proxyNova():
	url = 'http://www.proxynova.com/proxy-server-list/country-cn/'
	content = readContent(url)
	if content == False :
		return False
	return content

def writeToFile(filename,content):
	f = open(filename, 'a')
	for text in content:
		f.writelines(text+'\n\r')
	f.close()

def parseTable(text):
	data = []
	soup = BeautifulSoup(''.join(text))
	table = soup.find("table",{"class":"table"})
	table_body = table.find('tbody')
	for row in table_body.findAll("tr"):
	    cols = row.findAll("td")
	    try:
	    	data.append("http://"+str(cols[0].find("span").contents[0])+":"+ str(cols[1].find("a").contents[0]))
	    except:
	    	continue
	return data

writeToFile("proxylist1.txt",parseTable(proxyNova()))