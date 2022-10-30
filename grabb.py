import requests,re,sys

url = "https://zone-d.org/mirror/archive/"
kueri = sys.argv[1]

r = requests.get(url+kueri)

tbody = re.findall(r'<tbody>(.*?)<\/tbody>',r.text)
td = re.findall(r'<td>(.*?)<td>',tbody[0])
for a in td:
  if re.findall(r'(.*?):',a):
    pass
  else:
    p = re.findall(r'(.*?)\/(.*?)',a)
    if p:
      print(p[0][0])
    else:
      print(a)