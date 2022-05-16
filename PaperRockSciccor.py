import sys
import random
import inquirer

PRS = [
    inquirer.List ('prs',
    message= "Paper, Rock, Sciccor?",
    choices= ['Paper', 'Rock', 'Sciccor'])
]
a = ['Paper','Rock','Sciccor']


if PRS == random.choice(a):
    print (f"no winner, both player chose {a}")
