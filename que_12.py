# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed

def check_palindrome(string):
    if string == string[-1::-1]:
        return "palindrome String"
    else:
        return "Not a palindrome"

string=input("String= ")
print(check_palindrome(string))