import urllib2
import os
import BeautifulSoup import BeautifulSoup
import re
def check_proxy(proxy,url):
	proxyHandle = urllib2.ProxyHandler({'http':proxy})
	opener = urllib2.build_opener(proxyHandle)
	try:
		page = opener.open(url,timeout = 5)
	except:
		return False
	return True


# print check_proxy('http://123.30.211.95:3128','http://www.something.com/')


def getProxyList(filename):
	with open(filename) as f:
		lines = f.readlines()
	for line in lines:
		line = line.replace('\n', '')
	print lines

getProxyList('proxyList.txt')