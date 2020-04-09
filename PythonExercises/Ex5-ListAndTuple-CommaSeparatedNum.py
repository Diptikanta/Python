#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#This exercise takes a user input list of numbers separated by comma and extracts the numbers from it
#Display the list and display the tuple

vals= input("Enter the numbers list: ")

list= vals.split(',')
tuples = tuple(list)

print(list)
print(tuples)