name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("Yo are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
        
    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game.")
        
    else:
        print("Not a valid option. You lose!")
        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross or back)? ")
    
    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger, do you talk to them(yes or no)? ")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
                                
        elif answer == "no":
            print("You ignore the stranger and they are offended so they beat you to a pulp! YOU LOSE!")
            
        else:
            print("Not a valid option you lose!")
                
    elif answer == "back":
        print("You go back to the main road and investigate the area to come back with the correct path.")
    
    else:
        print("Not a valid answer tou lose!")
else:
    print("Not a valid option. You lose!")
    
print('Thank you for trying', name)