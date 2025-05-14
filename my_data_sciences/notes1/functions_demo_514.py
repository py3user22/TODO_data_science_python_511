"""051425 functions demo"""


#////////////////////////////////
#ex1 parameters, but no return value demo

def happy_birthday2(age, name):
    print(f"Happy Birthday {name} and congratulations on turning {age} years old!")

#ex2 no parameters, but a return value
import random

def get_lucky_number():
    lucky_num = random.randint(1, 100)
    return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()
print("Your lucky number is:", lucky_number)


#ex4 parameters & return value

def calc_sale_price(amount, member=True):
    # Insert code here
    if member:
        # Members receive a 15% discount (0.15)
        amount = amount - (amount * 0.15)
    else:
        # Non-members get a 5% discount (0.05)
        amount = amount - (amount * 0.05)

    # Round amount to two decimal places
    # Save back in the amount variable
    # Insert code here
    return round(amount, 2)
    # Return amount to the main program
    # Insert code here

    # Example price (already provided)


full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:", member_price)            # 127.92

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:", non_member_price)    # 142.97


# ex3 scope

def calculate_monthly_payment(principal: float, interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly payment for a fixed-rate loan.

    Args:
        principal: The total amount borrowed (float).
        interest_rate: The annual interest rate (as a decimal, float).
        loan_term_years: The loan term in years (int).

    Returns:
        The monthly payment amount (float).

    Raises:
        ValueError: If any of the inputs are negative or zero.

    Example:
        # >>> calculate_monthly_payment(100000, 0.05, 30)       #  530.33
    """

    if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
        raise ValueError("All input values must be positive.")

    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term_years * 12

    # Calculation logic for monthly payment (omitted for brevity)

    return monthly_payment



#ex5  original needs edits
global_sum = 0  # Global variable

def calculate_mean_with_side_effect(numbers):
    global global_sum  # Modifying a global variable
    global_sum = sum(numbers)
    return global_sum / len(numbers)

calculate_mean_with_side_effect([5, 3, 4, 1, 1])   # 2.8


#ex5.1  redo to make it more modular aka ' pure function '
def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

calculate_mean([5, 3, 4, 1, 1])    # 2.8


#ex7 circles measure

def calculate_diameter_circle(radius: float):
    """Calculates the diameter of a circle."""
    diameter = radius * 2
    if radius < 0:
        return -1
    else:
        return diameter

#////////////////////////////////

#ex temperature conversion tool

def celsius_to_fahrenheit(celsius):
    """"""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """"""
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature, unit):
    """"""
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Invalid unit")

"""
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")

output:
25°C is equal to 77.0°F
77°F is equal to 25.0°C
"""


#ex8
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Good morning")  # Output: Good morning, Bob!
greet("Carol", "Howdy")      # Output: Howdy, Carol!



#////////////////////////////////


#ex1 variable number of arguments
# use *args      --> to collect positional arguments into a tuple
# use **kwargs   --> to collect keyword arguments into a dictionary


def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

""" output:
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
"""


#ex w/ *args >> This function accepts any number of positional arguments and sums them.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10


#ex w/ **kwargs  >> This function iterates through keyword arguments and prints them.
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25, city="New York")








#////////////////////////////////

#ex1
def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = []

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)

"""
{'name': 'Alice', 'age': 25, 'occupation': 'Software Engineer', 'interests': ['Coding', 'Hiking']}
{'name': 'Bob', 'age': 18, 'occupation': 'Student', 'interests': []}
{'name': 'Carol', 'age': 30, 'occupation': 'Student', 'interests': ['Gardening', 'Reading']}
"""


#ex2 make sandwich
def make_sandwich(bread_type: str, filling: str, cheese=None, toasted=False):
    """
    Makes a sandwich.
    :param bread_type:
    :param filling:
    :param cheese:
    :param toasted: default is False
    :return:
    """

    if toasted == True:
        return f"Making a toasted {bread_type} sandwich with {filling}."
    else:
        return f"Making a {bread_type} sandwich with {filling}."

    if cheese == True:
        return f"Making a {bread_type} sandwich with {filling} and {cheese} cheese."
    else:
        return f"Making a {bread_type} sandwich with {filling}."

    return 0

#////////////////////////////////
#////////////////////////////////
