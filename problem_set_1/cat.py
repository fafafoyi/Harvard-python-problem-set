n = int(input("How many times should cat meow? "))

while True:
    n = int(input("How many times should cat meow? "))
    if n > 0 :
        break

print("meow\n" * n , end="")