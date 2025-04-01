def main():
    grocery_list = {}  

    print("Enter grocery items (Press Ctrl+D to finish):")
    try:
        while True:
            item = input().strip().lower()  
            
            if item:  
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
    except (EOFError, KeyboardInterrupt):  
        print("\n")  

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

main()