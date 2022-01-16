#!python3

people = ['Alainr\r', 'Brian\r', 'Chris\r', 'Justin\r', 'Angela\r', 'Rick\r']

print(people)

x = input("enter a word from the list")
y = input("enter another word")

p = [y if a==x else a for a in people]
print(p)

"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
