def product (a,b)

return a * b 

def weekday_name (day_of_week):

    DAYS = [
        "Sunday"
        "Monday"
        "Tuesday"
        "Wednesday"
        "Thursday"
        "Friday"
        "Saturday"
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

        return  DAYS [day_of_week - 1]


def last_element (lst):
    if lst: 
        return lst[-1]

def number_compare(a,b):

if a > b:
    return "First is greater"
elif b > a:
    return "Second is greater"
else: 
    return "Numbers are equal"

def reverse_string (phrase):
    return phrase [::-1]

def single_letter_count (word, letter):
    return word.lower().count(letter.lower())    

def multiple_letter_count (phrase):
    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr,0) + 1 

        return counter 

def list_manipulation(lst, command, location, value=None): 

    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning"
            lst.insert(0, value)
            return lst 
        elif location == "end":
            lst.append(value)
            return lst     


def is_palindrome(phrase):
    normalized = phrase.lower().replace('', '')
    return normalized == normalized[::-1]

def frequency(lst, search_term):
    return lst.count(search_term)

def flip_case(phrase, to_swap):

    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr 

    return out 

def multiple_even_numbers(nums):

    product = 1
    for num in nums: 
        if num % 2 == 0:
            product = product * num 
    return product 

def capitalize(phrase):
    return phrase.capitalize()

def compact(lst):

    return [val for val in lst if val]  

def intersection (l1, l2):
    set2 = set(l2)

    return [val for val in l1 if val in set2]  

def partition(lst, fn):

    true_list = []
    false_list = []

    for val in lst:
        if fn(val): 
            true_list.append(val)
        else: 
            false_list.append(val)
    return [true_list, flase_list]  

def mode(nums):
    counts = {}

    for num in nums: 
        counts [num] = counts.get(num, 0) + 1 

    max_value = max (counts.value())

    for (num, freq) in counts.items():
        if freq == max_value:
            return num 

def calculate (operation, a,b, make_int=False, message= 'The result is'):

    if operation == "add":
        res = a + b 
    elif operation == "substract":
        res = a - b 
    elif operation == "multiply":
        res a * b 
    elif operation == "divide":
        res = a / b 
    else: 
        return  

def friend_date(a, b):

    if set(a[2]) & set(b[2]):
        return True 
    else:
        return False g                                                                                                               
