"""051725 common exceptions"""

#ex1 to check the parameters are integer|floats
def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers.")
    return length * width

print(calculate_area(5, 'three')) # TypeError: Length and width must be numbers.


#ex2 check the length
my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])


#ex3 use try-except to catch a empty list
my_list = []
try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")


#ex4 check if key is in the dict..
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")


# using import logging to
import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError encountered: {e}")
    # Handle the error or provide a fallback mechanism


#ex6 making a method


def get_city_population(populations, city):
    try:
        return f"The population of {city} is {populations[city]}"
    except KeyError:
        return f"City {city} not found in population data."


city_populations_demo1 = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

population_data2 = {
    "Tokyo": 14000000,
    "New York": 8500000,
    "London": 9000000,
    "Paris": 2100000
}
demo = get_city_population(population_data2, "Houston")
print(demo)


#ex7 try-except demo2
def get_population(population_dict, city):
    try:
        return f"The population of {city} is {population_dict[city]}."
    except KeyError:
        return f"Sorry, {city} is not in the dictionary."

# Example usage:
population_data = {
    "Tokyo": 14000000,
    "New York": 8500000,
    "London": 9000000,
    "Paris": 2100000
}

city_name = input("Enter a city name: ")
print(get_population(population_data, city_name))


#//////////////////////

#ex1.  assertions demo
def calculate_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width


#ex2.  use the close() to free memory usage
"""
with Image.open(image_path) as img:
    # Process the image
    img.close()  # Explicitly close the image file
"""


#ex3  try-except demo
file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)


#ex4 try-except demo2
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data types")


#ex5 logging demo
import logging

try:
    # Your potentially error-prone code here
except Exception as e:
    logging.error(f"An error occurred: {e}")  # Logs the exception with details


#ex7 custom exceptions
"""
class InvalidCredentialsError(Exception):
    pass

# ... later in your code ...
if not valid_credentials(username, password):
    raise InvalidCredentialsError("Incorrect username or password")
"""

#ex8 make function demo
def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: File not found -", file_path)
    finally:
        file.close()


#//////////////////////
#//////////////////////
#//////////////////////
#//////////////////////
