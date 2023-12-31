def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True 

    return False         

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    while start <= stop:
        print (start)
        start = start + 1


count_up(5, 7)    


def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    for num in nums: 
        if num >= lowest and num <= highest: 
            print ("f"{num} "fits")


in_range([10, 20, 30, 40, 50], 15, 30)

def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    total = 0

    for num in nums: 
        total = total + num 

        return total 


print("sum_nums returned", sum_nums([1, 2, 3, 4]))


#OOP Python 

class SerialGenerator:

def __init__(self, start=0):
    self.start = self.next = start 

def __repr__ (self):
    return f"<SerialGenerator start={self.start} next={self.next}>"

def generate(self):
    self.next += 1 
    return self.next - 1 

def reset(self):
    self.next = self.start 

class WordFinder:

def _init_(self, path):
    dict_file = open(path)

    self.words = self.parse(dict_file)

    print(f"{len(self.words)} words read")

def parse(self, dict_file):
    return [w.strip() for w in dict_file]

def random(self):

    return random.choice(self.words)  


class SpeicalWordFinder(WordFinder):

    def parse(self, dict_file):

        return [w.strip() for w in dict_file
        if w.strip() and not w.startswith("#")]  

