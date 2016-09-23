from BeautifulSoup import *
import urllib
url=raw_input('Enter - ')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)

tags=soup('a')
for tag in tags:
    print tag.get('href',None)


#当HTML规范有序则用正则
import urllib
import re

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
    print link