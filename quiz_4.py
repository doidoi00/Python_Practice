web = "http://naver.com"
index = web.find("://")
index = index +3
nex = web.find(".")
now = web[index:nex]
last = now[:3]
print(now)
count = len(now)
how = now.count("e")
print(how)
print(last + str(count) + str(how) +"!")
