# Python code to check a given sequence is palindrome or not
my_string1 = input("Enter a string")
My_string1 = my_string1.casefold()
# reverse the given string
rev_string1  = reversed(my_string1)
# check whether the string is equal to the reverse of it or not
if list(my_string1) == list(rev_string1):
  print("It is a palindrome")
else:
  print("It is not a palindrome")
