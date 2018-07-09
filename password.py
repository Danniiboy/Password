import re

while True:
  name = input('What is your name:')
  if name.isalpha():
    print('Welcome',name)
    break
  elif name.isnumeric():
    print('You typed in a number we only accept letters')
  else:
    print('Please enter a name')

while True:
  password = input("Enter a password: ")
  if re.match(r'^((?!.*[@.,<>%\$/#^*!~`])(?!.*[\s])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,})', password):
    print ("Good job your password is: ",password)
    break
  else:
    print ("Nice Try! Try Again")
