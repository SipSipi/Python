""" Module Name: 

   Paper Rock Scissor mini game 

   Created By: Asif asif@schinkels.com.my 
   Created: 18/5/2022 
   Framework: Python 3.10 on localhost
   Last Edited: 22/5/2022 

   Reason Edited: Put comments
"""
# Source: library 
# process of asking end user questions, parsing, validating answers
import inquirer

# Source: library
# change variable declaration       
from optparse import Values

import sys

# Source: library
# get random selection
import random



UserPrompt = None # User choice to continue or exit
UserChoice = None # User choice from UserPrompt inquirer
dictPrs = None  # list of end user choices
dictC = ''  # end user selected choice 
listA = '' # list of computer choices
strB = '' # selected computer choice from listA

# User choose to play or not
UserPrompt = [                                  
        inquirer.List('prompt',
        message= "Do you want to play?",
        choices= ['Yes','No'])
        ]
UserChoice = inquirer.prompt(UserPrompt)        # Kept the user choice 

while str(*UserChoice.values())=='Yes' :        # everytime end user choose yes, the game starts
    # list of end user choices
    dictPrs = [
        inquirer.List ('prs',
        message= "Paper, Rock, Sciccor?",
        choices= ['Paper', 'Rock', 'Scissor'])
    ]

    dictC= inquirer.prompt(dictPrs) #get end user selection
    listA = ['Paper','Rock','Scissor']
    strB = str(random.choice(listA)) #randomly select computer choice from listA

        # determine whether end user selection win, or computer selection win
    if str(*dictC.values()) == strB : # *dictC.values change dict to string
        print (f"no winner, both player choose {strB}")
    elif str(*dictC.values()) == 'Paper' and strB == 'Rock':
        print ('Congrats ' + str(*dictC.values()) + ' win')
        print ( strB + ' lost ')
    elif str(*dictC.values()) == 'Rock' and strB == 'Scissor':
        print ('Congrats ' + str(*dictC.values()) + ' win')
        print ( strB + ' lost ')
    elif str(*dictC.values()) == 'Scissor' and strB == 'Paper':
        print ('Congrats ' + str(*dictC.values()) + ' win')
        print ( strB + ' lost ')
    else :
        print ( str(*dictC.values()) + ' You lose, ' + strB + ' win')
    
    UserPrompt = [                                  # Ask user whether the user want to play again or not
        inquirer.List('prompt',
        message= "Do you want to play again?",
        choices= ['Yes','No'])
        ]
    UserChoice = inquirer.prompt(UserPrompt)    

if str(*UserChoice.values())=='No':                 # this game is over when end user choose No
            print ('Thank you for playing')
