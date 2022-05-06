#functions of list
a= ['pink','purple','orange']#1
a.append('white')
print(a)

numbers=['1','2','3']#2
alphabets=['a','b','c']
numbers.extend(alphabets)
print(numbers)

A=['9','8','6']#3
print('before')
print('A:',A)
A.insert(2,'7')
print('after')
print('A:',A)

a1=['comp','program','python']#4
print('old')
print('a1:',a1)
a1.pop(0)
print('new')
print('a1:',a1)

num_1=[2,3,4,6,8,]#5
print(num_1)
num_1.remove(8)
print(num_1)

old_list=[1,2,3,4,5]#6
print(old_list)
new_list=old_list.copy()
print('updated list:',new_list)

t={1:'mango',2:'strawberyy'}#7
print(t)
t.clear()
print(t)

a='i found sea shells on sea shore.the sea is beautiful'#8
b=a.count('sea')
print('count is:',b)

veggies=['tomato','eggplant','ladyfinger','potato','onion']#9
a=veggies.index('ladyfinger')

num=['a','b','c','d','e','f','g']#10
num.reverse()
print(num)

x=[1,10,6,8,34,21]#11
x.sort()
print(x)

#functions of string
b="vegetables,potatoes"
y= b.capitalize()
print (y)

a="How Are You"
x=a.casefold()
print(x)

fruit="choclate"
mo=fruit.center(20)
print(mo)

amazon="you are there you go you come"
ok=amazon.count("you")
print(ok)

sen="statements in english"
ten= sen.endswith(".")
print(ten)

tex="t\u\v\w\xy"
exp=tex.expandtabs(2)
print(exp)

fi="where are you"
nd=fi.find("where")
print(nd)

shop="For only {price:.2f} dollars!"
print(shop.format(price = 10))

g="grapes,banana,apple"
k=g.index("banana")
print(k)

chk="covid19"
t=chk.isalnum()
print(t)

pc="laptop"
device=pc.isalpha()
print(device)

sta="Right567"
j=sta.isascii()
print(j)

txt="\u0036"
q=txt.isdecimal()
print(q)

d="2948"
_i=d.isdigit()
print(_i)

iden="is"
w=iden.isidentifier()
print(w)

low="awesome!"
ow=low.islower()
print(ow)

num="772694826"
nm=num.isnumeric()
print(nm)

correct="34_#.we"
ap=correct.isprintable()
print(ap)

run="   "
un=run.isspace()
print(un)

tile="Once Upon A Time"
ty=tile.istitle()
print(ty)

up="IS THIS OKAY"
u=up.isupper()
print(u)

my=("studies", "career", "job")
m="#".join(my)
print(m)

st="strawberry"
ra=st.ljust(10)
print(ra, "is my favorite fruit.")

er="Oh ReAlLy"
lw=er.lower()
print(lw)

spa="     chocolate     "
ce=spa.lstrip()
print("of all sweets", ce, "is my favorite")

hi="Hello SAP!"
mysent=hi.maketrans("S", "C")
print(hi.translate(mysent))

part="she is over there"
tio=part.partition("she")
print(tio)

hq="I like java"
iq=hq.replace("java", "python")
print(iq)

rf="hi there hi"
_r= rf.rfind("hi")
print(_r)

rch="hi there hi"
do=rch.rindex("hi")
print(do)

nc="tomato"
ert=nc.rjust(30)
print(ert, "is my favorite veg.")

cb="hello python,python is good"
sc=cb.rpartition("python")
print(sc)

hal="im, so, cherrful"
ot=hal.rsplit(", ")
print(ot)

txx="     apple     "
tt=txx.rstrip()
print("of all fruits", tt, "is my favorite")

invi="welcome to python world"
tato=invi.split()
print(tato)

awa="Thank you for your coordination\nhere is your award"
rd=awa.splitlines()
print(rd)

dry="indian society"
heat=dry.startswith("indian")
print(heat)

ewq="     apple     "
tiu=ewq.strip()
print("of all fruits", tiu, "is my favorite")

tom="I aM ToM hOlLaNd"
rex = tom.swapcase()
print(rex)

story="once upon a time"
til=story.title()
print(til)

mypy={83:  67}
thon= "Hello Sam!"
print(thon.translate(mypy))

pper="text is low"
upp=pper.upper()
print(upp)

home="5"
hous=home.zfill(30)
print(hous)


