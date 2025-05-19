"""051825 test demo """


def send_discount(books_purchased, discount_threshold):
    """
    :param books_purchased: num of books purchased
    :param discount_threshold: min num books needed for discount
    :return: print statement 1|2
    """
    if books_purchased <= discount_threshold:
        return "No discount."
    else:
        return "Discount applied!"

"""
send_discount(3, 5)  # Should print No discount.
send_discount(7, 5)  # Should print Discount applied!
"""


#-------------------------------------
#ex2, adding a parameter to 3
def send_discount(books_purchased, discount_threshold, bonus_threshold):
    """
    :param books_purchased: num of books purchased
    :param discount_threshold: min num books needed for discount
    :return: print statement 1|2|3
    """
    if books_purchased <= discount_threshold:
        return "No discount."
    elif books_purchased > bonus_threshold:
        return "Big discount applied!"
    else:
        return "Discount applied!"


#-------------------------------------
#ex3 loops for repetitive tasks demo
def categorize_ratings(rating_list):
    number_of_low_ratings = 0
    number_of_medium_ratings = 0
    number_of_high_ratings = 0

    for i in rating_list:
        if i >= 1 and i <= 4:
            number_of_low_ratings += 1
        elif i >= 5 and i <= 7:
            number_of_medium_ratings += 1
        elif i >= 8 and i <= 10:
            number_of_high_ratings += 1
        else:
            pass
    print(f"Low: {number_of_low_ratings}")
    print(f"Medium: {number_of_medium_ratings}")
    print(f"High: {number_of_high_ratings}")


#categorize_ratings([1, 3, 5, 7, 8, 9])


#-------------------------------------
#ex4 sorting list demo
#step1: create list
students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]
#step2: create dict test scores
test_performance = {
    "John": 87,
    "Lisa": 90,
    "Mary": 75,
    "Chris": 100,
    "Linda": 100,
    "Matt": 70,
}
#step3: extract the scores of dict
scores = []
for val in test_performance.values():
    scores.append(val)

# print(scores)
#step4: sort scores w/ custom function
def bubble_sort(scores_list):
    sorted_scores = sorted(scores_list)
    return sorted_scores

demo_sc_list = scores

sorted_scores = bubble_sort(demo_sc_list)
print(sorted_scores)    # [70, 75, 87, 90, 100, 100]

#/////////////////////////////////


#Task2, step1: calculate high& low scores
lowest_score = sorted_scores[0]
highest_score = sorted_scores[-1]

print(f"Lowest Score: {lowest_score}")     #70
print(f"Highest Score: {highest_score}")   #100


#step2: average function
def average_class_score(sorted_scores_list):
    length_list = len(sorted_scores_list)
    if length_list == 0:
        return 0
    else:
        return sum(sorted_scores_list) / length_list

average_score = average_class_score(sorted_scores)
print(average_score)  # 87.0
print(f"Highest Score: {highest_score}")    # Highest Score: 100
print(f"Lowest Score: {lowest_score}")      # Lowest Score: 70
print(f"Average Score: {average_score}")    # Average Score: 87.0

