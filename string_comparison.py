s1 = "banana"
s2 = "bob"

print(s1 > s2)
print("bob is greater than banana", s2 > s1)

# lowercase is always higher than uppercase (due to ASCII code)

s1 = "banana"
s2 = "Banana"
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)

# you pretty much always compare with ==

#we can use operators with strings
print("a"in "banana")
print("banana" in "banana")
print("ana" in "banana")
print("bob" in "banana")
