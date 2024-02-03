def is_palindrome(word):
    cleaned_word = "".join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

str1 = input('Enter a word or phrase:')
if is_palindrome(str1):
    print('Its a Palindrome')
else:
    print('Its not a Palindrome')
