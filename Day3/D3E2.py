# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight/(height**2)
if BMI < 18.5:
    print("Your BMI is %i, you are underweight" %(round(BMI)))
elif BMI < 25:
    print("Your BMI is %i, you have a normal weight" %(round(BMI)))
elif BMI < 30:
    print("Your BMI is %i, you are slightly overweight" %(round(BMI)))
elif BMI < 35:
    print("Your BMI is %i, you are obese" %(round(BMI)))
else:
    print("Your BMI is %i, you are clinically obese" %(round(BMI)))
