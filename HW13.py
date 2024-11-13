#Name: Chaysen Wise
#Class: 5th Hour
#Assignment: HW13

#1. Create a list containing 10 integers of your choice.
sillyIntList = [1, 2, 6, 11, 12, 16, 21, 22, 26, 10]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = (0)
oddNumbers = (0)
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in sillyIntList:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

# Print the total count of even and odd numbers.

print("there are", evenNumbers, "even numbers")
print("there are", oddNumbers, "odd numbers")