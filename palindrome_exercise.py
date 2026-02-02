from string import punctuation

s = "Red Roses run no risk, sir, on nurses order."
s = "yo! banana boy"
# prove that this sentence is a palindrome!!
# 1. sanitize (remove space and remove other punctuation)
punctuation = " !.,:;?"
for p in punctuation:
    s = s.replace(p, "")
print(s)

# 2. make it all same case (lower or uppercase). use: .lower() method
s = s.lower()
print(s)

# 3. compare that the slice of reverse is the same as the original

if s == s[::-1]: # string is the same as in reverse
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

