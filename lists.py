spam = ['cat', 'dog', 'bird', 'koala', 'dog', 'kangaroo']
eggs = [12, 78, 100, 54, 42]
foo = [12.5, 1.78, 3.14159]
person = ('Matt', 50, 185.0)
tic_tac_toe = [
  ['', 'O', ''],
  ['X', 'O', ''],
  ['', 'X', '']
]

# name = person[0]
# age = person[1]
# height = person[2]
# name, age, height = person
# print(f'{name} is {age} years old and {height}cm tall')

# for index, animal in enumerate(spam):
#   print(f'{index + 1}. {animal}')
spam.sort(reverse=True)
print(spam)
