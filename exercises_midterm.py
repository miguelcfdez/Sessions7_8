#text = input("Enter a string: ")

#index = len(text) - 1   # start from last character --> Python starts counting at 0

#while index >= 0:
#print(text[index])
#index -= 1

# Now we take a palindrome and turn it the other way around to make sure it is a palindrome
palindrome = "Yo, banana boy!"
punctuation = " !.,:;?"
for p in punctuation:
    palindrome = palindrome.replace(p, "")
palindrome = palindrome.lower() # we put it in lowercase letters
print(palindrome[::-1])
print(palindrome)

def is_palindrome(s):
    s = s.lower()
    for p in punctuation:
        s = s.replace(p, "")
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("banana"))
print(is_palindrome("Racecar"))
print(is_palindrome("Yo, banana boy!"))

def is_palindrome(s):
    punctuation = ",.!?:;'\"()[]{}- "

    s = s.lower()

    for p in punctuation:
        s = s.replace(p, "")

    return s == s[::-1]

print(is_palindrome("banana"))
print(is_palindrome("Racecar"))
print(is_palindrome("Yo, banana boy!"))

# Both ways work

word = input("Enter a word: ")
word = str(word)

if word == "":
    print("Invalid input")
else:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    n_consonants = 0
    n_digits = 0

    for c in word.lower():
        if c in vowels:
            n_vowels += 1
        elif c.isdigit():
            n_digits += 1
        elif c.isalpha():
            n_consonants += 1

    if n_vowels > n_consonants:
        print("More vowels")
    elif n_consonants > n_vowels:
        print("More consonants")
    else:
        print("Equal vowels and consonants")

    print("Digits:", n_digits)