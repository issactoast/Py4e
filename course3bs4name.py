from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
count = int(count)
pos = input('Enter position: ')
pos = int(pos) - 1

mycount = 0
while True:
    if mycount == count: break
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[pos].get('href')
    print(url)
    mycount = mycount + 1
name = tags[pos].contents[0]
print('Name', name)
