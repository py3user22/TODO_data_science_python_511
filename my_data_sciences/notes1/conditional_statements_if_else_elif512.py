"""051225' conditional statements
    if, elif, else
"""

# ex1 great function
def greet(name):
    """greeting msg including the name"""

    name = "Hello " + str(name) + "!"

    return name

result = greet("Jesus Gomez")
# print(result)   # Hello Jesus Gomez

# /////////////////////////////


# ex2 nested functions & scoping demo

def outer_function(x):
    """outer function that takes integer x, adds 1500, then calls an inner function"""

    y = x + 1500

    def inner_function():
        """inner function multiplies y x 2"""

        z = y * 2
        print("inside inner function, z =", z)

    inner_function()   # calls the inner function
    print("Inside outer function, y =", y)

outer_function(700)
""" output:
inside inner function, z = 4400
Inside outer function, y = 2200
"""

#/////////////////////////////////////

"""
ex.3  for loops, counting from 10-0 backwards

for x in range(10, -1, -1):   if x ==5: print("special message").  else: print(x)

"""


#ex 515  count vowels function
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

"""
sentence = "This is a test sentence to count vowels."
vowel_count = string_utils.count_vowels(sentence)
print("Number of vowels:", vowel_count)   # 12
"""
#/////////////////////////////////////

# installing many modules at once

# pip install django djangorestframework django-cors-headers

"""
Django: This is the core web framework that provides the structure and tools for building your web application.

djangorestframework: If you're building a RESTful API (a way for different applications to communicate with each other over the web), this library simplifies the process of creating and managing APIs in Django.

django-cors-headers: Modern web applications often involve interactions between different domains (origins). This library helps you configure Cross-Origin Resource Sharing (CORS) in your Django project, ensuring secure communication between your front end and back end.
"""


#/////////////////////////////////////

# ex2 dict call
# Create a dictionary to store contact information
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Look up Bob's phone number
bobs_phone = contacts["Bob"]
print(bobs_phone)
# Output: 555-5678

# Add a new contact
contacts["David"] = "555-4321"

# Update Carol's phone number
contacts["Carol"] = "555-2468"

# Remove Alice's contact information
del contacts["Alice"]

# Print updated contacts
print(contacts)   # {'Bob': '555-5678', 'Carol': '555-2468', 'David': '555-4321'}

#/////////////////////////////////////

# Values provided (do not change)
array = [1, 2, 2, 3, 1, 4, 5, 3]

# The following line will need to change to only store unique values
unique_set = set(array)  # YOUR CODE HERE

# List conversion and print provided (do not change)
unique_array = list(unique_set)
print(unique_array)  # [1, 2, 3, 4, 5]



