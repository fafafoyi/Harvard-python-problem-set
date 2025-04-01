def main():

    food_list =  {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }   
    output = addition(food_list)
    print(output)
   

def addition(x):

    total_cost= 0.00

    try:
        while True:

            item = input().strip().title()

            if item in x:
                total_cost += x[item]
                print(f"total: ${total_cost: .2f}")
            else:
                continue
        
                
    
    
    
    
    except (EOFError, KeyboardInterrupt):
            print("\nFinal total: ${:.2f}".format(total_cost))


    
    
main()