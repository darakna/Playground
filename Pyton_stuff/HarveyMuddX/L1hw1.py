__author__ = 'darakna'
comp = 'elefant'
user = 'indian' # this line is changed during the video

if comp == 'paper' :
    if user == 'paper' :
        print ("Tie")
    elif user == "rock":
        print ("You win")
    elif user == "scissors":
        print ("I win")

elif comp == "rock":
    if user == 'paper':
        print ('I win')
    elif user == "scissors":
        print ('I win!')
    else:
        print ("Tie")
else:
    if user == 'paper' :
        print ("You win")
    elif user == "rock":
        print ("I win")
    else:
        print ("Tie")
