"""
For & While Loops
"""

my_list = [1, 2, 3, 4, 5]

for iterator in my_list :
    print(iterator)

#####################################################

for x in my_list :
    print(x)

#####################################################

for x in range(3, 6) :
    print(x)

#####################################################

sum_of_for_loop = 0

for x in my_list :
    sum_of_for_loop += x

print(sum_of_for_loop)

#####################################################

str_list = ["Mon", "Tues", "Wen", "Thu"]

for x in str_list :
    print(x)

#####################################################

i = 0

while i < 5 :
    i += 1
    print(i)

#####################################################

i = 0

while i < 5 :
    i += 1
    if i == 3 :
        continue
    print(i)

#####################################################

i = 0

while i < 5 :
    i += 1
    if i == 3 :
        continue
    print(i)
else :
    print("i is now larger or equal to 5")

#####################################################

i = 0

while i < 5 :
    i += 1
    if i == 3 :
        continue
    print(i)
    if i == 4 :
        break
else :
    print("i is now larger or equal to 5")
    
#####################################################