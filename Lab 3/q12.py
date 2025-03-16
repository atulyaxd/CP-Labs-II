l = []

for i in range(0,3):
    x = int(input("enter num"))

    l.append(x)
  
o = []
for i in l:
    o.append((i,pow(i,3)))

print(o)