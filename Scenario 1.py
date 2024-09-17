#Name: Chaysen Wise
#Class: 5th hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.


enemyDict = {
"Slime" : {
   "Attack" : "30",
   "Defense" : "30",
   "Speed" : "40",
},
"Kitsune" : {
   "Attack" : "50",
   "Defense" : "30",
   "Speed" : "60",
},
"Cursed Armor": {
   "Attack": "60",
   "Defense": "70",
   "Speed": "20",
},
"Mimic": {
   "Attack": "50",
   "Defense": "50",
   "Speed": "30",
},
"Skeleton": {
   "Attack": "40",
   "Defense": "40",
   "Speed": "40",
}
}


print(enemyDict)



slimeNewAttack = input("choose a new value for slime's attack")
kitsuneNewAttack = input("choose a new value for kitsune's attack")
cursedArmorNewAttack = input("choose a new value for cursed armor's attack")
mimicNewAttack = input("choose a new value for mimic's attack")
skeletonNewAttack = input("choose a new value for skeleton's attack")

enemyDict = {
"Slime" : {
   "Attack" : slimeNewAttack,
   "Defense" : "30",
   "Speed" : "40",
},
"Kitsune" : {
   "Attack" : kitsuneNewAttack,
   "Defense" : "30",
   "Speed" : "60",
},
"Cursed Armor": {
   "Attack": cursedArmorNewAttack,
   "Defense": "70",
   "Speed": "20",
},
"Mimic": {
   "Attack": mimicNewAttack,
   "Defense": "50",
   "Speed": "30",
},
"Skeleton": {
   "Attack": skeletonNewAttack,
   "Defense": "40",
   "Speed": "40",
}
}



print(enemyDict)