school ={
  "student":"tom",
  "age": "17",
  "year": 2004
}
school.clear()
print(school)
#############
iid= {
  "student":"tom",
  "age": "17",
  "year": 2004
}
y=iid.copy()
print(y)
############
t=('have', 'want', 'give')
m=1
thi=dict.fromkeys(t, m)
print(thi)
###########
grocery={
  "noneed":"chocolates",
  "have":"chicken",
  "bring":"vegetables"
}
q=grocery.get("bring")
print(q)
##########
person={
  "place":"india",
  "state":"maharashtra",
  "year":2022
}
g =person.items()
print(g)
##########
pers={
 "place":"india",
  "state":"maharashtra",
  "year":2022
}
j= pers.keys()
print(j)
#########
son={
 "place":"india",
  "state":"maharashtra",
  "year":2022
}
son.pop("state")
print(son)
########
jack= {
  "time":"evening",
  "venue":"dontknow",
  "when":"tomorrow"
}
jack.popitem()
print(jack)
###########
car={
  "brand":"toyota",
  "model":"rav4",
  "year":2015
}
h=car.setdefault("model")
print(h)
###########
car={
  "brand":"mclaren",
  "model":"mclaren F1",
  "year":1998
}
car.update({"color": "fluroscent orange"})
print(car)
##########
carss={
  "toyota":"prado",
  "color": "white",
  "number":1
}
i=carss.values()
print(i)
