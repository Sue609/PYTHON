#Enter help to continue playing the game
command = input(">")

if command == "help":
    print("""
    start - to start the car
    stop  - to stop thecar
    quit  - to exit
    """)
  
command = input(">")  
if command == "start":
    print("Car started... Ready to go!")
 
command = input(">")  
if command == "stop":
    print("Stop the car...I've reached my destination")

command = input(">")   
if "help" == "quit":
    exit
    
command = input(">")
if command != "start" and command != "stop" and command != "exit":
    print("I do not understand!")
    