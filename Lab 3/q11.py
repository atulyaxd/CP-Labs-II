a = (5,20,3,7,6,8)
a = tuple(sorted(a))
n = len(a)
d1 = a[:n//2]
d2 = a[n//2:]

d1 = tuple(i for i in d1 if i != max(d1))
d2 = tuple(i for i in d2 if i != min(d2))
d3 = d1 + d2
print(d3)
"""

a_l = []
for i in a:
    a_l.append(i)

for i in a_l:
    if i == max or i == min:
        a_l.remove(i)
a_l.sort()
soln = tuple(i for i in a_l)
print(soln)


# Alternative

b = tuple(i for i in a if i != max)
b = tuple(i for i in b if i != min)


print(tuple(sorted(b)))
"""


