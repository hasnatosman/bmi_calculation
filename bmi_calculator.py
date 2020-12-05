print('BMI calculator to check Body Mass Index.!')


# how to find bmi......................
def BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# driver code..........................
weight = int(input('Input your weight in kg :'))
height = float(input('Input your height in metre :'))

# calling the BMI function.............
bmi = BMI(weight, height)
print('The BMI is', format(bmi), ', So it looks you are ', end=' ')

if bmi < 18.5:
    print('underweight.')
elif 18.5 < bmi < 24.9:
    print('healthy.')
elif 24.9 < bmi < 30:
    print('overweight.')
elif bmi > 30:
    print('suffering from the obesity.')
