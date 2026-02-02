s1 = "hello world"
s2 = 'hello world'
print(s1)
print(s2)

s1 = "hello world (/&%!@/$&"
print(s1)
print(s1[1]) # starts counting from 0, so position 1 is e (h is 0)
print(s1[-1])
print(s1[-4])
print(len(s1)) # the amount of characters in the string
print(s1[len(s1)-1]) # the last character, instead of -1, same as line 9

# index needs to be integer!
print(s1[8//4])

# you can add 2 strings: you get a string back!!!
print(s1+s2)

# you can multiply a string via an integer!
print(s1*3)
print(4*s2)

s1 = "I am very angry"
s2 = "!"*20
print(s1+s2)

# you can iterate over a string via for
for c in s1:
    print(c*5, end="") # Forces everything to be in one line

for c in s1:
    if c == " ":
        print("?", end="")
    else:
        print(c, end="")
print()


