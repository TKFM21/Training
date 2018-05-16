def palindrome(word):
    word = word.lower()
    if word[::-1] == word:
        return word.capitalize()
    else:
        return False

print(palindrome('Mother'))
print(palindrome('Mom'))
print(palindrome('Pop'))
input()
