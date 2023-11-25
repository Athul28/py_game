import random

choices=['rock','paper','scissors']

bot_points=0
user_points=0

c=random.choice(choices)
print(c)

def point(user_choice,bot_choice):
    if(user_choice=='rock' and bot_choice=='paper'):
        bot_choice+=1
    elif(user_choice=='rock' and bot_choice=='scissors'):
        user_choice+=1
    elif(user_choice=='paper' and bot_choice=='rock'):
        user_choice+=1
    elif(user_choice=='paper' and bot_choice=='scissors'):
        bot_choice+=1
    elif(user_choice=='scissors' and bot_choice=='rock'):
        bot_choice+=1
    elif(user_choice=='scissors' and bot_choice=='paper'):
        user_points+=1

i=1
while(i<=5):
    print("----------------------------")
    print("1.ROCK\n2.PAPER\n3.SCISSOR\n")
    while(True):
        try:
            user_choice=int(input("Enter your choice : "))
        except Exception as e:
            print("Enter a number\n")