import urllib2
import os
import re


def writeToFile(filename,content):
	f = open(filename, 'a')
	for text in content:
		f.writelines(text+'\n\r')
	f.close()

def writeStringToFile(filename,string):
	f = open(filename,'a')
	f.writelines(text+'\n\r')
	f.close()

def check_proxy(proxyList,url):
	# okList = []
	for proxy in proxyList:
		
		try:
			proxyHandle = urllib2.ProxyHandler({'http':proxy})
			opener = urllib2.build_opener(proxyHandle)
			page = opener.open(url,timeout = 5)
			# writeStringToFile('listAliveProxy.txt', proxy)
			print "checking "+ proxy +" is alive"
		except KeyboardInterrupt:
			print "thank for you using!"
			break
		# except:
		# 	print "checking "+ proxy +" is dead"
		# 	continue
	# 	okList.append(proxy)
	# writeToFile('listAliveProxy.txt', okList)


# print check_proxy('http://123.30.211.95:3128','http://www.something.com/')


def getProxyList(filename):
	with open(filename) as f:
		lines = f.readlines()
	lines = [word.strip() for word in lines]
	return lines

check_proxy(getProxyList("listProxy.txt"),'http://www.something.com/')