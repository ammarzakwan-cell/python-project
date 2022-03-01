print('BMI Calculator')

weight, height = input('Enter your weight(kg) and height(m): ').split()
weight, height = [float(weight), float(height)]

bmi = weight/height**2

print('BMI: ', round(bmi, 2))

if bmi<18.5:
    result = 'Underweight'
elif 18.5<=bmi<=24.9:
    result = 'Healthy'
elif 25.0<=bmi<=29.9:
    result = 'Overweight'
else:
    result = 'Obese'

print('Category: ', result)