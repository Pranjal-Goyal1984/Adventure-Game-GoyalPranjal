import random

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

# what happens when the user chooses something

while (user!="q"):
  distance = random.randint(20,40)
  medium = random.randint(10,17)
  enemy = random.randint(5,10)
  med_enemy = random.randint(1,6)
  if(user == "a" or user == "stop and eat and drink water"):
    thirstLevel = 0
    enemyDistance = enemyDistance - random.randint(1,5)
    hungerLevel = 0
    print("\nYou stop to eat and drink.\nThirst and hunger increase.\nThe humans continue the chase.\n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "b" or user == "status check"):
    print("\nYou traveled "+str(distanceTraveled) + " miles. \nThe humans are " + str(enemyDistance)+" miles away. \nYour fuel is at " + str(fuelLevel)+". \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "c" or user == "stop and refill your engine"):
    enemyDistance = enemyDistance - random.randint(1,4)
    fuelLevel = 10
    print("\nYou stop to refill your engine. \nThe fuel level is back up to 10. \nThe humans continue the chase. \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "d" or user == "full speed"):
    distanceTraveled = distanceTraveled + distance
    enemyDistance = enemyDistance - 5 + enemy
    thirstLevel = thirstLevel + 4
    hungerLevel = hungerLevel + 3
    fuelLevel = fuelLevel - 5
    print("\nYou traveled " + str(distance) + " miles. \nThirst and hunger increase \nFuel decreases \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(user == "e" or user == "moderate speed"):
    distanceTraveled = distanceTraveled + medium
    enemyDistance = enemyDistance - 10 + med_enemy
    thirstLevel = thirstLevel + 2
    hungerLevel = hungerLevel + 1
    fuelLevel = fuelLevel - 3
    print("\nYou traveled " + str(medium)+ " miles. \n thirst and hunger increase \nFuel decreases \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(thirstLevel >= 6):
    print("\nYou need to drink water. \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(hungerLevel >= 7):
    print("\nYou need to eat. \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(fuelLevel <= 4):
    print("\nFuel is starting toget real low! \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(enemyDistance <= 25):
    print("\nYou start to see the humans' ship behind you! \n" + str(options))
    user = input("\nYour choice: ").lower()
  if(enemyDistance >= 150):
    print("You have succeeded in escaping the humans and are now happily on your way home. ")
  if(fuelLevel <= 0):
    print("Your fuel has run out and you ended up being captured by the humans, who took you to Area 51 to be researched. ")
  if(hungerLevel >= 10):
    print("You forgot to eat and therefor disengrated, atleast the humans didn't get body, I guess. ")
  if(thirstLevel >= 10):
    print("You forgot to drink water and therefor disengrated, atleast the humans didn't get body, I guess. ")
  if(enemyDistance <= 10):
    print("The humans were able to capture and elimate you, making sure that none of your kind would ever reach them again. ")



if(user == "q"):
  print("\nLooks like this is an adventure for next time!")