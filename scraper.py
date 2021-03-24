import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificare errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="https://journal-abbreviations.library.ubc.ca/dump.php"
data=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(data,'html.parser')
righe=soup.findAll('table')[0].tbody.findAll('tr')

a=0
for row in righe:
    a+=1
    first_column=row.findAll('td')[0]
    second_column=row.findAll('td')[1]
    print(f"{second_column.contents[0]};{first_column.contents[0]}")
    if a>14:
        break

print("OK")
print("OK")