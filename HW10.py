#Name: Chaysen Wise
#Class: 5th hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
import time
i = 5
while i >= 0:
    print(i)
    time.sleep(0.1)
    i -= 1
else:
    print("Hello World")


#2. Create a while loop that prints only even numbers
#between 1 and 30.
b = 0
while b < 30:
    print(b)
    time.sleep(0.1)
    b += 2


#3. Create a while loop that repeats until the user
#inputs the number 0.
y = 1
while y >= 1:
    print("type 0 pls")
    time.sleep(0.8)
    y += 1
    z = int(input())
    if z == 0:
     break