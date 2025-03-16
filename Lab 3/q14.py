#Aim : A intersection B

A = {1,2,3,4}
B = {3,6,7,8}

res = set()
"""
for i in A:
    if i in B:
        res.add(i)

print(res)

#Aim : A union B
res2 = set()
for i in A:
    res2.add(i)
for j in B:
    res2.add(j)

print(res2)
"""
#Alternative
c = A.union(B)
print(c)
d = A.intersection(B)
print(d)