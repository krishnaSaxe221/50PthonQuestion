def palindrome(str):
    if(str==str[-1::-1]):
        print("The letter is palindrome:")
    else:
        print("Not a palindrome:")
str=input("Enter the string:")
palindrome(str)
