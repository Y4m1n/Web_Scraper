#import urllib

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     url=urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
import urllib
import json
url=raw_input("Enter location: ")
print "Retrieving", url
data=urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
info=json.loads(data)
sum=0
for item in info["comments"]:
    sum=item["count"]+sum

print "Sum:",sum
