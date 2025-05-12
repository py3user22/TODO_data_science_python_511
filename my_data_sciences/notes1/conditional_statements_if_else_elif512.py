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