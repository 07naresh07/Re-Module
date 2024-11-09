import re
import urllib.request
from urllib.parse import quote

try:
    url = "https://www.dictionary.com/browse/"
    word = input("Enter your word: ")
    url += word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    print(data1)

except:
    print("An unsolvable error has occured!!!")

