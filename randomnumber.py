import sys
import random

guess = 0
rand_num = random.randint(1,10)

while guess!=rand_num:
    if guess > rand_num :
        print ("your number is too high")
    elif guess < rand_num :
        print ("your number is too low")
    guess = int(input("please enter your number between 1 - 10 :"))
print (f"congrats, you got it. the number is {rand_num}")
