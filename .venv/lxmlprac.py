from io import BytesIO
from lxml import etree
import requests

url = 'http://10.0.2.15/'
r = requests.get(url) # Get request
content = r.content() # Content type of bytes

parser = etree.HTMLParser()
content = etree.parse(BytesIO(content), parser=parser) # Parse into a tree


for link in content.findall('//a'):
    print(f'{link.get('href')} -> {link.text}')