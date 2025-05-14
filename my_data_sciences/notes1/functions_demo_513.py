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
#/////////////////////////////
