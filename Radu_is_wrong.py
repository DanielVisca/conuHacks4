import urllib.request, sys, bs4
url = "http://data.alexa.com/data?cli=10&dat=s&url="+ "http://breitbart.com"
print(bs4.BeautifulSoup(urllib.request.urlopen(url)).find("REACH")['RANK'])