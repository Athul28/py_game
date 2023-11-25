import random

choices=['rock','paper','scissors']

global bot_points
bot_points=0
global user_points
user_points=0

def point(user_choice,bot_choice):
    global bot_points
    global user_points
    if(user_choice=='rock' and bot_choice=='paper'):
        bot_points+=1
        print("Bot gets a point")
    elif(user_choice=='rock' and bot_choice=='scissors'):
        user_points+=1
        print("You get a point")
    elif(user_choice=='paper' and bot_choice=='rock'):
        user_points+=1
        print("You get a point")
    elif(user_choice=='paper' and bot_choice=='scissors'):
        bot_points+=1
        print("Bot gets a point")
    elif(user_choice=='scissors' and bot_choice=='rock'):
        bot_points+=1
        print("Bot gets a point")
    elif(user_choice=='scissors' and bot_choice=='paper'):
        user_points+=1
        print("You get a point")
    else:
        print("No points")

i=1
for i in range(5):
    print("----------------------------")
    print("1.ROCK\n2.PAPER\n3.SCISSOR\n")
    while(True):
        try:
            user_choice=int(input("Enter your choice : "))
            break;
        except Exception as e:
            print("Enter a number")
    bot_choice=random.choice(choices)
    print("Your choice : ",choices[user_choice-1])
    print("Bot choose : ",bot_choice)
    point(choices[user_choice-1],bot_choice)
    print("Your Score : ",user_points)
    print("Bot Score : ",bot_points)

print("\n----------------------------")
if(user_points>bot_points):
    print("YOU WON!!!")
elif(user_points<bot_points):
    print("You lost, better luck next time")
else:
    print("It's a draw")
print("----------------------------")