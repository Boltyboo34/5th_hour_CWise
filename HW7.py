#Name: Chaysen Wise
#Class: 5th hour
#Assignment: HW6

print ("Hello World!")

#1. Print Hello World!

#2. Create three different boolean variables named wifi, login, and admin.

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".



Wifi = True
Login = True
Admin = False

numOfLogin = 6

if Wifi == True:
    if Login == True:
        if Admin == True:
            numOfLogin = 7
            print("Welcome Sillygoose")
else:
