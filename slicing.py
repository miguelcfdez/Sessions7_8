s = "hello world!"
print(s[5]) # indexing, one letter

# slide 1, from start to end
print(s[2:7])
print(s[3:5]) # last one is always excluded (5 in this case)
print(s[2:4]) # for instance, this prints 2 and 3

# you can omit the start or the end, or both
print(s[:7]) # from beginning to pos 7 (excluded)!
print(s[3:])
print(s[:]) # the entire string

# there is another thing, we can add a step :)
print(s[::2])
print(s[4::3])
print(s[::-1])