from optparse import Values
import sys
import random
import inquirer

PRS = [
    inquirer.List ('prs',
    message= "Paper, Rock, Sciccor?",
    choices= ['Paper', 'Rock', 'Scissor'])
]



c= inquirer.prompt(PRS)
a = ['Paper','Rock','Scissor']
b = str(random.choice(a))

if str(*c.values()) == b :
    print (f"no winner, both player choose {b}")
elif str(*c.values()) == 'Paper' and b == 'Rock':
    print ('Congrats ' + str(*c.values()) + ' win')
    print ( b + 'lost ')
elif str(*c.values()) == 'Rock' and b == 'Scissor':
    print ('Congrats ' + str(*c.values()) + ' win')
    print ( b + 'lost ')
elif str(*c.values()) == 'Scissor' and b == 'Paper':
    print ('Congrats ' + str(*c.values()) + ' win')
    print ( b + 'lost ')
else :
    print ( str(*c.values()) + ' You lose, ' + b + ' win')  
