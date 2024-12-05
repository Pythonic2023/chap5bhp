from io import BytesIO
from lxml import etree
import requests

url = 'http://192.168.122.76/DVWA'
r = requests.get(url) # Get request
content = r.content # Content type of bytes

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser) # Parse into a tree
print('-'*50)
print(content)
print('-'*50)
for link in content.findall('.//a'):
    print(f'{link.get('href')} -> {link.text}')