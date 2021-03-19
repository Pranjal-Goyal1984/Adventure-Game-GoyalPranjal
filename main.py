print("Welcome to Escape!\nYou are an alien trying to reach the space jump point to escape from the humans. ")

#user choices

options = ("\nWhat do you want to do?\nA. Stop and eat and Drink water\nB. Status Check\nC. Stop and refill your engine\nD. Full speed \nE. Moderate speed\nQ. Quit game")
print(options)

#user choice

user = input("\nYour choice: ").lower()

#variables

distanceTraveled = 0
thirstLevel = 0
hungerLevel = 0
enemyDistance = 30
fuelLevel = 10

# what happens when the user chooses A.

while (user!="q"):
  if(user == "a" or user == "stop and eat and drink water"):
    thirstLevel = 0
    enemyDistance = enemyDistance - 2
    hungerLevel = 0
    print("\nYou stop to eat and drink.\nThirst and hunger decrease.\nThe humans continue the chase.\n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "b" or user == "status check"):
    print("You traveled "+str(distanceTraveled) + " miles. \nThe humans are " + str(enemyDistance)+" miles away. \nYour fuel is at " + str(fuelLevel)+". \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "c" or user == "stop and refill your engine"):
    enemyDistance = enemyDistance - 3
    fuelLevel = 10
    print("You stop to refill your engine. \nThe fuel level is back up to 10. \nThe humans continue the chase. \n" + str(options))
    user = input("\nYour choice: ").lower()


if(user == "q"):
  print("\nLooks like this is an adventure for next time!")