import sys
import random
import inquirer

PRS = [
    inquirer.List ('prs',
    message= "Paper, Rock, Sciccor?",
    choices= ['Paper', 'Rock', 'Sciccor'])
]

a = ['Paper','Rock','Sciccor']

c = inquirer.prompt(PRS).
#print (c)

if c == random.choice(a):
    print (f"no winner, both player chose {a}")
elif c != random.choice(a)[1] :
    print (str(c) + 'win')
elif c != random.choice(a)[2] :
    print (str(c) + 'win')
elif c != random.choice(a)[0] :
    print (str(c) + 'win') 
else :
    print (random.choice(a) + ' win')  
