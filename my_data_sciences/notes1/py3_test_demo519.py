"""051925 test demo"""


def send_discount(books_purchased, discount_threshold):
    if books_purchased <= discount_threshold:
        print("No discount.")
    else:
        print("Discount applied!")

demo1 = send_discount(3, 5)
demo2 = send_discount(7, 5)


# print(demo1)
# print(demo2)
print("---------------------------------\n")


def send_discount(books_purchased, discount_threshold, bonus_threshold):
    if books_purchased >= bonus_threshold:
        print("Big discount applied!")  # Priority for big discount first
    elif books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")


demo3 = send_discount(books_purchased=3, discount_threshold=5, bonus_threshold=10)
demo4 = send_discount(books_purchased=7, discount_threshold=5, bonus_threshold=10)
demo5 = send_discount(books_purchased=12, discount_threshold=5, bonus_threshold=10)


# print(demo3)  # Output: No discount.
# print(demo4)  # Output: Discount applied!
# print(demo5)  # Output: Big discount applied!
print("---------------------------------\n")

#//////////////////////////////


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

demo6 = categorize_ratings([1, 3, 5, 7, 8, 9])
# print(demo6)
print("---------------------------------\n")
"""
Low: 2
Medium: 2
High: 2
None
"""

#//////////////////////////////

# activity3: sorting test scores w/ error handling
#step1:
students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]

#step2: create a dict of test scores
test_performance = {
    "John": 87, "Lisa": 90, "Mary": 75, "Chris": 100, "Linda": 100, "Matt": 70,
}

#step3: extract the scores from dict
scores_list = []
for val in test_performance.values():
    scores_list.append(val)


scores_list2 = scores_list

#step4: create function, to list scores in asc. order
def bubble_sort(list_here):
    sort_list1 = sorted(list_here)
    return sort_list1

demo_sort = bubble_sort(scores_list2)
# print(demo_sort)  # [70, 75, 87, 90, 100, 100]

#step5: assign the sorted variable to new var. ' sorted_scores '
sorted_scores = demo_sort
print(sorted_scores, '\n')  # [70, 75, 87, 90, 100, 100]

#task2, step1: get high&low score
lowest_score = sorted_scores[0]
highest_score = sorted_scores[-1]

print(f"Lowest Score: {lowest_score}")      # Lowest Score: 70
print(f"Highest Score: {highest_score}")    # Highest Score: 100


#t2, step2: make function for class average w/ error handling for empty list
def average_class_score(score_list):
    length = len(score_list)
    if length == 0:
        raise ValueError("Score list cannot be empty.")
    else:
        return sum(score_list) / length

demo_avg = average_class_score(sorted_scores)
print(demo_avg)  # 87.0



