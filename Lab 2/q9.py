name,age,weight,height = "Atulya", 19, 80, 1.8


BMI = weight / pow(height,2)
remarks = ""
if(BMI < 18.5): 
    remarks = "Underweight"

elif (BMI >= 18.5) and (BMI < 24.9):
    remarks = "Healthy Weight"
    
elif (BMI >= 25) and (BMI < 29.9):
    remarks = "Overweight"

elif (BMI >= 30):
    remarks = "obese"
    
print("{}, {}, {}, {:2f}, {}, {}".format(name,age,height,weight, BMI, remarks))