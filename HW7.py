#Name: Chaysen Wise
#Class: 5th hour
#Assignment: HW7

print ("Hello World!")


Wifi = False
Admin = True
Login  = False

numOfLogin = 2

if Wifi == True:
    if Login == True:
        if Admin == True:
            numOfLogin += 1
            print("Welcome Sillygoose")

else:
    if Wifi == False:
        print("You are missing wifi")
        exit()
    if Admin == False:
        print("You are missing Admin")
        exit()
    if Login == False:
        print("You are missing Login")

print(numOfLogin)