#this is for Palindrome 
#created by aryan#

def checkif_palindrome(x):
	return x == x[::-1]

x = "madam"
Final = checkif_palindrome(x)

if Final:
	print("Yes")
else:
	print("No")
