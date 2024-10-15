#Name: Chaysen Wise
#Class: 5th hour
#Assignment: Scenario 2

print ("Hello World!")

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

#Step 1: Copy enemy dictionary from SC1

#Step 2: Copy party dictionary from SC2

#Step 3: Make sure every enemy and party member has health points (fixed)

#Step 4: Make sure every enemy and party member has an attack modifier (fixed)

#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)

#Step 6: Make every enemy and party member has a damage roll (random)

#Party Dictionary Goes Here



#Enemy Dictionary Goes Here



#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member

#Step 8: Pick an ememy

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive


#Combat Code Goes Here

import random

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

partyDict = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Attack Modifier" : 10,
        "Damage Roll": random.randint(1,6) + random.randint(1,6)+3,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Attack Modifier" : 5,
        "Damage Roll": random.randint(1,6)+2,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Attack Modifier" : 6,
        "Damage Roll": random.randint(1,10)
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Attack Modifier" : 12,
        "Damage Roll": random.randint(1,6) + 4,
    }
}

enemyDict = {
"Slime" : {
   "Attack Modifier" : 30,
   "Health" : 5,
    "Damage Roll": random.randint(1,6) + random.randint(1,6),
    "AC" : 11,
},
"Kitsune" : {
   "Attack Modifier" : 50,
   "Health" : 30,
    "Damage Roll": random.randint(1,6) + random.randint(1,6),
    "AC" : 13,
},
"Cursed Armor": {
   "Attack Modifier": 60,
   "Health": 70,
    "Damage Roll": random.randint(1,6) + random.randint(1,6),
    "AC" : 17,
},
"Mimic": {
   "Attack Modifier": 50,
   "Health": 50,
    "Damage Roll": random.randint(1,6) + random.randint(1,6),
    "AC" : 17,
},
"Skeleton": {
   "Attack Modifier": 40,
   "Health": 40,
    "Damage Roll": random.randint(1,6) + random.randint(1,6),
    "AC" : 17,
}
}

if  random.randint(1,20) + partyDict["Gale"] ["Attack Modifier"] >= enemyDict["Slime"] ["AC"]:
    enemyDict["Slime"] ["Health"] -= partyDict["Gale"] ["Damage Roll"]
    print("Gale's attack hit")
    if enemyDict["Slime"]["Health"] <= 0:
        print("the slime is dead")
        exit()
    else:
        print("the slime is alive")
else:
    print("Gale's attack missed")

if  random.randint(1,20) + enemyDict["Slime"] ["Attack Modifier"] >= partyDict["Gale"] ["AC"]:
    partyDict["Gale"] ["Health"] -= enemyDict["Slime"] ["Damage Roll"]
    print("Slime's attack hit")
    if partyDict["Gale"]["Health"] <= 0:
        print("Gale is dead")
        exit()
    else:
        print("Gale is alive")
else:
    print("The slime's attack missed")
