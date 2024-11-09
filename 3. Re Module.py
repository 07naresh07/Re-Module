import re
string="Hello. My name is Naresh Singh Dhami"
m = re.search("Naresh",string)
start=m.start()-8 #goes to the -8 position from the start i.e Naresh (N is start and h is end
end=m.end()+5
print(string[start:end]) #or we can write: print(strin[m.start():m.end()])
