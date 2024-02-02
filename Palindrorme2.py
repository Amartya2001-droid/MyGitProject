#this is for Palindrome 
#created by aryan#

def checkif_palindrome(x):
	return x == x[::-1]

s = "madam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
