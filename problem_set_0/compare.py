def main():
    x = int(input("Whats'x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):

    return n % 2 == 0
   
    
    

main()