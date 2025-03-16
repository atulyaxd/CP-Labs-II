#working with lists 
list1 = ["Red", "Blue", "Green", "Yellow"]


list1.append("White") #added a new color
#list1.pop(1) #remobed 2nd color from list
list1.remove("Blue")

print(list1)

#woking with tuple

list2 = ("Red", "Blue", "Green", "Yellow")
#list2[1] = "White" #Error encountered
print(list2)

#working with Dictionary
dict1 = {1: 'Red', 2:'Blue', 3:'Green', 4:'Yellow'}
dict1[2] = "White"
print(dict1)

#working with sets
set1 = {"Red", "Blue","Green", "Yellow"}
set1.add("White")  #Set - Mutable
set1.add("Red") #Outcome = Index of color changed
print(set1)