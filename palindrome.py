x=str(input("enter a word:"))
reverse=x[::-1]
print(reverse)
if x==reverse:
    print("is palindrome")
else:
    print("not palindrome")
