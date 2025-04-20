import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symblos = "!@#$%^&*()_+<>-=[]"
all_chars = lower + upper + numbers + symblos
length = int(input("enter a length:"))
password = ''. join(random.sample(all_chars, length))
print("generated password:", password)
