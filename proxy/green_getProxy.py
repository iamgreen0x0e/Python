import urllib2
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
def readContent(url):
	response = urllib2.urlopen(url)
	try:
		return response.read()
	except:
		return False

def writeToFile(filename,content):
	f = open(filename, 'a')
	for text in content:
		f.writelines(text+'\n\r')
	f.close()

def proxyNova():
	country = ['cn','ve','tw','in','br','id','us','th','ru','ar','hk','de','eg','jp','cl','ma','co','vn','bd','ua','gb','pl','my','fr']
	for count in country:
		writeToFile("listProxy.txt",parseTableProxyNova(proxyNovaCountry(count)))
		print "done in "+count
def proxyNovaCountry(country):
	url = 'http://www.proxynova.com/proxy-server-list/country-'+ country+'/'
	content = readContent(url)
	if content == False :
		return False
	return content



def parseTableProxyNova(text):
	data = []
	soup = BeautifulSoup(''.join(text))
	table = soup.find("table",{"class":"table"})
	table_body = table.find('tbody')
	for row in table_body.findAll("tr"):
	    cols = row.findAll("td")
	    try:
	    	proxy = "http://"+str(cols[0].find("span").contents[0])+":"+ str(cols[1].find("a").contents[0])
	    except AttributeError:
	    	try:
	    		proxy = "http://"+str(cols[0].find("span").contents[0])+":"+ str(int(cols[1].contents[0]))
	    	except:
	    		continue
	    data.append(proxy)
	return data

proxyNova()