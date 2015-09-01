import urllib2
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup


def readContent(url):
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	response = urllib2.urlopen( req )
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

# def getIdXroxy():
# 	req = urllib2.Request("http://www.xroxy.com/proxylist.php?country=IL", headers={'User-Agent' : "Magic Browser"}) 
# 	con = urllib2.urlopen( req )
# 	html = con.read()
# 	# print html
# 	data = ''
# 	soup = BeautifulSoup(html)
# 	content = soup.findAll("select",{"id":"country_id"})
# 	for option in content[0].findAll("option"):
# 		data +='\''+option['value']+'\','
# 	return data


def XroxyCountry(country):
	url = "http://www.xroxy.com/proxylist.php?country="+country
	content = readContent(url)
	if content == False:
		return False
	return content

def parseTableXroxy(text):

	data =[]
	soup = BeautifulSoup(text)
	table = soup.findAll("table")
	for counter in range(0,2):
		rows=table[4].findAll("tr",{"class":"row"+str(counter)})
		for row in rows:
			column = row.findAll("td")
			data.append("http://"+column[1].find("a").contents[0].strip()+":"+column[2].find("a").contents[0])
	return data	



def Xroxy():
	proxyCountryList = ['AF','AL','DZ','AR','AU','AT','BD','BE','BO','BW','BR','BG','KH','CA','CL','CN','CO','CZ','DK','DO','EC','EG','EE','FR','GE','DE','GH','GB','GR','HK','IN','ID','IR','IQ','IE','IL','IT','JP','KZ','KE','KR','LV','MG','MY','MV','MU','MX','MD','MN','NP','NL','NG','PK','PA','PY','PE','PH','PL','PT','PR','RO','RU','SN','SC','SG','SK','SO','ZA','ES','LK','SE','CH','TW','TJ','TH','TN','TR','UA','US','VE','VN','ZW']
	for count in proxyCountryList:
		writeToFile("listProxy.txt",parseTableXroxy(XroxyCountry(count)))
		print "done in "+count

proxyNova()