f_name = "Atulya"
l_name = "Bharat"
btach_no = "24EE"
roll_no = 13

#method 1 
print("Full name:",f_name,"", l_name,", roll no:",roll_no)

#method 2
print("Full name: {1} {2}, roll no: {0}".format(roll_no,f_name,l_name))

#method 3
print("Full name:",f_name,l_name,sep="", end=",")
print("roll no :",roll_no)

#method 4
print(f"Full name: {f_name} {l_name}, roll no: {roll_no}")

#method 5
print("full name: %s %s, roll no: %d"%(f_name, l_name, roll_no ) )