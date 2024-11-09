import re
import urllib.request
url = "https://www.google.com/finance/quote/"
stock = "META"
url=url+stock
data = urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
print(data1)