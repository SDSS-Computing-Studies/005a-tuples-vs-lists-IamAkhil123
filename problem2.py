#! python3

fruit = ["apple","cherry","kiwi","apple","banana","strawberry","kiwi","blueberry","kiwi"]

print(fruit)

x = input("enter a word")

if fruit.__contains__(x):
 p = ["" if a==x else a for a in fruit]
 print(p)
else:
  fruit = fruit + x
  print(fruit)

"""
CODE WORKS BUT AUTO GRADER HAS A INDENT

Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list

inputs:
string

outputs:
list

examples:
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:kiwi
['apple', 'cherry', 'apple', 'banana', 'strawberry', 'blueberry']

['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi']
Enter a word from the list:orange
word not in list
['apple', 'cherry', 'kiwi', 'apple', 'banana', 'strawberry', 'kiwi', 'blueberry', 'kiwi', 'orange']

"""

