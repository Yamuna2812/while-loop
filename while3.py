text = input("Enter a word: ")
reverse = ""
i = len(text) - 1

while i >= 0:
    reverse += text[i]
    i -= 1

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")