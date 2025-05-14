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





#////////////////////////////////
#////////////////////////////////
#////////////////////////////////
#////////////////////////////////
#////////////////////////////////
