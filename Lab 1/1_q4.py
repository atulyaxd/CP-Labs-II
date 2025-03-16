hour = int(input("Enter Hours: "))
min = float(input("Enter minutes: "))

print("Entered time in seconds",end="= ")

seconds = 3600*hour + 60*min

print(seconds)