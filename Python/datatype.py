a=[50,60,70,30]
a.append(50)
print(a)

b=[8,9,7,4,35,78]
b.insert(0,9)
print(b)

c=[9,7,3,6,8]
c.pop(3)
print(c)
c.pop()
print(c)

d=[4,6,8,9,20]
d[0]=2
print(d)

a=(4,89,20,38,46)
b=list(a)
print(b)

n={3,7,8,9,4}
n.add(6)
print(n)
n.remove(3)
print(n)

m={

    "Name":"Ammu",
    "Age":22,
    "Place":"Nagercoil"

}
m["Age"]=23
print(m)
print(m.keys())
print(m.values())
d={
    "Name":["Ammu","Bachi","Jayasree"], 
    "Age":[22,23,46]

    }
print(d)
