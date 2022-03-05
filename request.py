import json
import requests

a=requests.get('http://saral.navgurukul.org/api/courses')
g=a.json()
with open("requ.json","w") as f:
    json.dump(g,f,indent=4)

s=[]
count=0
for i in g['availableCourses']:
    print(count,i['name'],i['id'])
    s.append(i["id"])
    count+=1


num=int(input("enter your counting num :")) 
c=0
b=requests.get("http://saral.navgurukul.org/api/courses/"+s[num]+"/exercises")
# print(b)
m=b.json()
print(m)
l=[]
for i in m["data"]:
    print(c,i["slug"])
    l.append(i["slug"])
    c=c+1
num2=int(input("enter your slug num:"))
k=requests.get("http://saral.navgurukul.org/api/courses/"+str(num)+"exercise/getBySlug?slug="+l[num2])
o=k.json()
print(o)

