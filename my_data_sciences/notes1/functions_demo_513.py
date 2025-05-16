"""051325 functions demo"""


#/////////////////////////////
"""
# syntax of functions
---------------------

def function_name(parameters):
    \"\"\"docstring explaining what function does\"\"\"
    # code to perform the task
    return result   # return statement to close
"""

#ex1 rectangle area
def calculate_rectangle_area(length, width):
  """Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  # Your code here
  area = length * width
  return area


#/////////////////////////////

# ex2. temperatures demo513
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = antarctic_temperatures ### Insert code here
high2 = max(antarctic_temperatures)
lowest_temp = antarctic_temperatures ### Insert code here
low2 = min(antarctic_temperatures)

print("Highest temperature:", high2, "°C")
print("Lowest temperature:", low2, "°C")

# Calculate the average temperature
average_temp = antarctic_temperatures ### Insert code here
sum1 = sum(antarctic_temperatures)
len1 = len(antarctic_temperatures)
average_temp2 = round(sum1 / len1, 1)

print("Average temperature:", average_temp2, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = antarctic_temperatures ### Insert code here
coldest_temp_abs2 = abs(low2)
print("The coldest temperature was", coldest_temp_abs2, "°C below freezing.")

print("-----------------------------------\n ")

#/////////////////////////////

# ex3.
int_value = 15
float_value = 4.1
text_value = "33"

type_of_float_value = type(float_value) # STEP 2: YOUR CODE HERE

# Convert text_value to an integer
text_value_as_int = int(text_value) # STEP 3: YOUR CODE HERE

# Convert int_value to text
int_value_as_text = str(int_value) # STEP 4: YOUR CODE HERE

# DO NOT CHANGE LINES BELOW
# Print the type of float_value
print("float_value type:", type_of_float_value)

# Adding text_value_as_int to int_value
print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

# Adding (concatenating) text values
print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)


#/////////////////////////////

#ex4  classes demo
# encapsulation -->
class BankAccount:
  def __init__(self, balance):
    self._balance = balance  # Private attribute

  def deposit(self, amount):
    self._balance += amount

  def get_balance(self):
    return self._balance


#ex5  abstraction -- module > ' abc '  >> (abstract base classes)
# serve as blueprints for other classes, outlining essential methods that subclasses must implement

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        return "Bark!"


# ex6 character class demo
class Character:
  def __init__(self, name, health, strength, speed):
    self._name = name
    self._health = health
    self._strength = strength
    self._speed = speed



#ex7 car class
  class Car:
    def __init__(self, make, model, year, color):
      self.make = make
      self.model = model
      self.year = year
      self.color = color
      self.fuel_level = 100  # Initial fuel level

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")


#ex8 dog class
class Dog:
  def __init__(self, name, breed):
    self._name = name
    self._breed = breed

  def bark(self):
    print(f"Woof! My name is {self._name}, and I am {self._breed}.")

# Creating the instance of the Dog class (step 4)
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark (step 5)
my_dog.bark()


#/////////////////////////////


#ex9 function w/ no parameters

def happy_birthday():
    print("Happy Birthday @ 051425!")

happy_birthday()

#/////////////////////////////

# ex10 creating values for a dictionary
students_info = {}  # blank dict

students_info['Alice'] = {'Grade': 90, 'Contact': 'alice@example.com'}
students_info['Bob'] = {'Grade': 85, 'Contact': 'bob@example.com'}
students_info['Carol'] = {'Grade': 95, 'Contact': 'carol@example.com'}


# ex10.1   create {} and values
# Add the SKU data provided to the product catalog dictionary
product_catalog = {}

product_catalog['SKU123'] = {'Name': 'Widget A', 'Price': 19.99, 'Quantity': 50}
product_catalog['SKU456'] = {'Name': 'Gadget B', 'Price': 34.95, 'Quantity': 25}
product_catalog['SKU789'] = {'Name': 'Gizmo C', 'Price': 9.99, 'Quantity': 100}

print(f"The price of {product_catalog['SKU123']['Name']} is ${product_catalog['SKU123']['Price']}")
"""output:  >>  The price of Widget A is $19.99"""



#////////////////////////////////////////
#ex2
# Defining the dictionary
products = {
    "item1": {"name": "Laptop", "price": 1200, "stock": 10},
    "item2": {"name": "Phone", "price": 800, "stock": 25},
    "item3": {"name": "Tablet", "price": 450, "stock": 15}
}

# Printing name and price from the nested dictionary
for key, value in products.items():
    print(f"Product: {value['name']}, Price: ${value['price']}")



#ex3 specific entry called
# Defining the dictionary
products = {
    "item1": {"name": "Laptop", "price": 1200, "stock": 10},
    "item2": {"name": "Phone", "price": 800, "stock": 25},
    "item3": {"name": "Tablet", "price": 450, "stock": 15}
}

# Accessing name and price of item1
item1_name = products["item1"]["name"]
item1_price = products["item1"]["price"]

# Printing the values
print(f"Product: {item1_name}, Price: ${item1_price}")

#////////////////////////////////////////

#ex11
shopping_list = ["apples", "bananas", "milk"]  # List for items
item_quantities = {"apples": 3, "bananas": 1}  # Dictionary for quantities

# User adds an item
shopping_list.append("eggs")
item_quantities["eggs"] = 12

# User increases the quantity of bananas
item_quantities["bananas"] += 2

# User removes apples
shopping_list.remove("apples")
del item_quantities["apples"]

# Print updated list and dictionary
print(shopping_list)
print(item_quantities)

"""
['bananas', 'milk', 'eggs']
{'bananas': 3, 'eggs': 12}
"""


#ex12  create a cart
# Create an empty list to represent the shopping cart
shopping_cart = []

# Add items to the shopping cart
shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")

print("Shopping Cart:")
# Print the contents of the shopping cart
for item in shopping_cart:
    print(item)


#///////////////////////////////
#ex tuples () & sets {}

# Tuples
coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day

# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates