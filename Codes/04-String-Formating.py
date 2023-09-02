# String Formating

first_name = "Amin"
print("Hi " + first_name)
print (f"Hi {first_name}")

sentence = "Hi {}"
print(sentence.format(first_name))

f_name = "Amin"
l_name = "Shahnani"
greeting = "Hi, {} {}"
print(greeting.format(f_name, l_name))
print(f"Hi, {f_name} {l_name}, How are you?")