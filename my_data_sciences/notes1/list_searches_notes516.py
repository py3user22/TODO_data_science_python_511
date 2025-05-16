"""051625 notes"""

# binary search -- *must be sorted,
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#////////////////

# linear search -- unsorted & small

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
        return -1

    for i in range(len(data)):
        try:
            if data[i] == target:
                return i
            else:
                continue
                return -1
        except Exception as e:
            return "No data found. Try again"
    return -1


#////////////////  demo in operator search

fruits = ["apple", "banana", "cherry"]

# check if banana in list
if "apple" in fruits:
    print("Apple is in the fruit list.")
else:
    print("Apple is not in the fruit list.")


# ex. sorting cards, demo1
def simple_sort(cards):
  sorted_cards = []
  while cards:
    lowest_card = min(cards)
    sorted_cards.append(lowest_card)
    cards.remove(lowest_card)
  return sorted_cards

#ex. demo2
def quicksort(cards):
  if len(cards) < 2:
    return cards  # Base case: Already sorted if 0 or 1 element
  else:
    pivot = cards[0]  # Choose first card as pivot
    less = [i for i in cards[1:] if i <= pivot]
    greater = [i for i in cards[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


#////////////////
#////////////////
#////////////////
