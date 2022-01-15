#!python3


my_str = "Cat Fish Dog Bear Turtle"

words = [word.lower() for word in my_str.split()]

words.sort()

x = int(input("Enter the index for an animal:"))

if x < 1:
 print("The animal at that index is Bear")
if x < 2 and x > 0:
 print("The animal at that index is Cat")
if x < 3 and x > 1:
 print("The animal at that index is Dog")
if x < 4 and x > 2:
 print("The animal at that index is Fish")
if x < 5 and x > 3:
 print("The animal at that index is Turtle")

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""