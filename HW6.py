#Name: Chaysen Wise
#Class: 5th hour
#Assignment: HW6

print ("Hello World!")

num = 12

if num % 2 == 0:
    if num % 3 == 0:
        print (num / 3)
        print (num / 2)
    else:
        print ("num is not divisible 3")
        print (num / 2)
else:
    if num % 3:
        print ("num is not /2")
        print (num / 3)
    else:
        print ("num is not divisible by 2 or 3")