weight=float(input("Enter your weight: "))
height=float(input("Enter your height in meter:"))
bmi=round(weight/height**2)
if(bmi<18.5):
    print(f"Your BMI is {bmi} and you are underweight ")
elif bmi<25:
    print(f"Your BMI is {bmi} and you have normal weight ")
elif bmi<30:
    print(f"Your BMI is {bmi} and you are overweight ")    
elif bmi<25:
    print(f"Your BMI is {bmi} and you need to consult a doctor ")