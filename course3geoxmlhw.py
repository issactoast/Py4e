import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User input
mynum = input('Enter url number: ')

# Make url
url = serviceurl + mynum + ".xml"

# retrieve page and result
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

commentinfo = ET.fromstring(data)
results = commentinfo.findall('comments/comment')
print('Comment count:', len(results))
sum = 0
for item in results:
    comment_num = item.find('count').text
    sum = sum + int(comment_num)
print(sum)
