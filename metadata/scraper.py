my_file=open(r'C:\Users\sergi\Desktop\Code\FromBibTexToELEDIA\journal_abbreviations2.txt','r')
stringone=my_file.read()
stringone=stringone.replace('<\/tr>','').replace('<\/td>','')
righe=stringone.split('<tr>')
a=0
file_output=open("journals_abbreviations2.txt",'w+')

for r in righe:
    a+=1
    colonna=r.split('<td>')
    if colonna[0]=='' and r!='':
        file_output.write(f"{colonna[2].strip()};{colonna[1].strip()}\n")

my_file.close()
file_output.close()
print('ok')
'''
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
    first_column=row.findAll('td')[0].contents[0]
    second_column=row.findAll('td')[1].contents[0]
    #print(f"{second_column.contents[0]};{first_column.contents[0]}")
    if a>14:
        break

print("OK")
print("OK")
'''