'''
Question:
Write a Python program that checks whether a sentence is a palindrome,
ignoring spaces, punctuation, and capitalization.
'''

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

cleaned = ""
for ch in sentence:
    if ch.isalnum():  
        cleaned += ch

if cleaned == cleaned[::-1]:
    print("It's a palindrome sentence.")
else:
    print("Not a palindrome sentence.")
