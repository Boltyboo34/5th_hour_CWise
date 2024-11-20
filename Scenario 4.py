#Name: Chaysen Wise
#Class: 5th hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.


sillySum = 0

while True:
    try:
        playerCount = int(input("Please enter the number of players in this game"))
        if playerCount < 1:
            playerCount = int("b")
        else:
            break
    except ValueError:
        print("no, bad.\n")

for i in range (0, playerCount):
    while True:
        ratings = int(input("Please give a rating of 1 through 5"))
        if 1 > ratings or ratings > 5:
            print("bruh")
            continue
        else:
            sillySum += ratings
            break

print("The overall rating was",sillySum/playerCount)