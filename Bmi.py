height=float(input("please enter your height;"))
weight=int(input("Please enter your weight;"))
#to calculate bmi of different patients
print(height,weight)
bmi= weight/(height**2)
if bmi<18.5:
   
   print(f"Your BMI is:{bmi}.Your underweight")
elif bmi >=18.5<25:
    print(f"Your BMI is {bmi}.You have ae normal weight")
elif bmi>=25<30:
    print(f"Your BMI is {bmi}.You are slightly overweight")
elif bmi>=30<35:
    print(f"Your BMI is {bmi}.You are slightly obese")
else:
    print (f"Your BMI is{bmi}.You are obese.")  