# print the multiplication table until 10

for i in range(1, 11):
   for j in range(1, 11):
    print(f"{i} X {j} = {i * j}")

for i in range(1, 11):
   for j in range(i, 11): # this removes the repeated multiplications (2x5=5x2)
    print(f"{i} X {j} = {i * j}")

