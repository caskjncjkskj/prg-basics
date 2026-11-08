first = input("Enter first letter: ")
last = input("Enter last letter: ")
number_of_letters = ord(last) - ord(first) - 1
print(f"Between {first} and {last} are {number_of_letters} letters")
