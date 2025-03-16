import math
T = []
n = 5
i = 1
while i <= n:
    T.append(int(input("Enter Temp= ")))
    i += 1

size = len(T)
mean = sum(T) / size

num = 0
for i in T:
    num += pow(i-mean,2) 

sd = math.sqrt(num/size)
print(f"mean = {mean}, standard deviation = {sd}")