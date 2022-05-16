from asynchat import simple_producer
import sys

name = input(" Enter your name : ")
age = input (" Enter your age : ")
weight = float(input (" Enter your weight(kg) :"))
height = float(input ("Enter your height(cm) :"))
bmi = weight / ((height/100)**2)
print ("Hi " + name + "," + age)
print ("your BMi is " + str(bmi))
if bmi < 18.5:
    print('Underweight')
if bmi>=18.5 and bmi<25:
    print("Normal")
if bmi >= 25 and bmi < 30:
   print('Overweight')
if bmi >= 30:
   print('Obesity')