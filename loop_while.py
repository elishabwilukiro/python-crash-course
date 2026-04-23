
# while loop = Execute some code while condition remain true


'''
name = input("Enter your name: ")
if name == "":
     print("Please enter your name")
else:
     print(f"Welcome, {name}")
'''

'''
name = input("Enter your name: ")
while name == "":
     print("You did not enter your name")
     name = input("Enter your name: ")
print(f"Welcome, {name}")
'''

'''
food = input("Enter a food you like (q to quit): ")
while not food == "q":
     print(f"You like {food}")
     food = input("Enter another food: ")
print("bye")
'''


number = int(input("Enter a number between 1 - 10: "))
while number < 0 or number > 10:
     print(f"{number} is not valid")
     number = int(input("Enter a number between 1 - 10: "))
print(f"You number is {number}")