"""051125 notes for data sciences w/ python """


Microsoft_python_dev = {
    0: 'https://www.coursera.org/programs/m-uq19a/professional-certificates/microsoft-python-developer?',
    0.1: '------------------  in progress ',
    1: '24hr -- Python programming fundamentals',

        # todo
    2: '20hr -- Data analysis & visualization w/ python',
    3: '26hr -- Automation & Scripting w/ python',
    4: '22hr -- Web development w/ python',
    5: '21hr -- Advanced python development techniques',
    6: '19hr -- Project development w/ python',
}

#//////////////////////////////////// notes

"""
# install jupyter notebook using pip
>> pip install notebook

# to open jupyter notebook on cmd line
>> jupyter notebook 
jupyter notebook


# for i loop syntax
---------------------------
for i in range(start, end):
    # Code block to be executed repeatedly
    
------------------------------------

range(stop)    
ex.1
range(5)  >> loops from 0-4
------------------------------------

range(start, stop)
ex1
range(1, 11) >> loops from 1-10
------------------------------------

range(start, stop, step)
ex1
range(1, 10, 2)    >>> 1,3,5,7,9

range(10, 5, -1)   >>> 10,9,8,7,6
------------------------------------

while condition:
    # Code block to be executed repeatedly
    
number = 1
while number <= 10:
    print(number) 
    number = number + 1
    

ex1
option = 0
while option != 4:
    print("1. Perform action 1")
    print("2. Perform action 2")
    print("3. Perform action 3")
    print("4. Quit")
------------------------------------

Lists & loops
ex1.
-------
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
fruit_length = len(fruits)
print(fruit_length)
fruits.append("date")

ex2.
-------
students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Hello,", student)
    
for i in range(0,len(students)):
    print("Hello,", students[i])
    

ex3. while loops, simulate a dice roll 
-------
import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6) 
    print("You rolled a", roll)
    
    
ex4. calculate the sum of numbers from 1-100
-------
total = 0
for number in range(1, 101): 
    total += number
    print("The sum is:", total)


ex5. filter even numbers from a list
-------
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])       #>>  2, 4
    index += 1


Nested loops
ex1.
-------
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j, end="\t") # Print the equation
    print() # Move to the next line after each row
    

ex2.
-------
max_value = 50
for x in range(max_value +1):
    if (x%3 == 0) and (x%4 == 0):
        print(x)   
        
        
ex3.
--------     
valid_input = False
while not valid_input:
  user_input = int(input("Please enter a number greater than 0: "))
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")
    
    
ex4.
--------
player_score = 80

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")
  

ex5
-------
import random

# Set the secret_number variable here (between 1 and 10)
secret_number = 7
# Initialize the guess variable here with a value of 0
guess = 0
while guess != secret_number: # Add the while loop condition here
	guess = random.randint(1, 10)
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)


ex6
-------
temperature = 22  # Example temperature

if temperature < 20:
    print("It might be cold! You might need a jacket.")
else:
    print("It's warm! Enjoy the sunshine.")


ex7.
------
temperature = 15  # Let's assume the temperature is 15 degrees Celsius

if temperature < 10:
    print("Wear a jacket! It's cold out there.")
elif 10 <= temperature < 20:
    print("A light sweater should be fine. It's a bit chilly.")
elif 20 <= temperature < 30:
    print("Enjoy the pleasant weather! No need for extra layers.")
else:
    print("It's hot! Stay hydrated and wear sunscreen.")
    


ex8.
------
# Example: Keep asking for input until the user enters "quit"
user_input = ""
while user_input != "quit":
    user_input = input("Enter something (or 'quit' to exit): ")
    print("You entered:", user_input)
    

ex9.
-------
numbers = [3, 9, 1, 10, 5, 2, 8]

### Your code here
for num in numbers:
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
            
"""
