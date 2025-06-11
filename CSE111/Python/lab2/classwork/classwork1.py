def calculate_bmi(height,weight):

  height=height/100
  BMI=weight/(height**2)

  if 0<BMI<18.5:
    return "underweight"

  elif 18.5<BMI<24.9:
    return "Normal"

  elif 25<BMI<30:
    return "Overweight"

  elif BMI>30:
    return "Obese"

height=int(input("Enter the customer height:"))
weight=int(input("Enter the customer weight:"))
h=height/100
BMI=weight/h**2
print(f'Score is {BMI:.1f}.''You are',calculate_bmi(height,weight))
