"""
Lists are a collection of data
"""

my_list = [90,80, 70, 60, 50]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[3])

people_list = ["Amin", "Ali",  "Mohammad"]
print(people_list)
print(people_list[-1])

animals = ["Cat", "Dog", "Wolf", "Cow"]
print(animals)
print(animals[0])
animals[0] = "Owl"
print(animals[0])

cars = ["BMW", "OPEL", "NISSAN", "TOYOTA", "MAZDA", "KMC"]
print(cars[0:2])
print(cars[1:3])

numbers = [90, 12, 23, 45, 56,]
print(numbers)
numbers.append(1000)
print(numbers)
numbers.insert(2, 345)
print(numbers)
numbers.remove(45)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.sort()
print(numbers)
