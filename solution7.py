string = input("Enter a string: ")
new_string = ""
for char in string:
  if char not in new_string:
    new_string += char
if len(new_string)%2 == 0:
  print("CHAT WITH HER!")
else:  print("IGNORE HIM!")