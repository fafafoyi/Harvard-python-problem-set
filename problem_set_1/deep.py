def main():
    quest = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
 
    if answer(quest):
        print("Yes")
    else:
        print("No")

def answer(x):

    x = x.strip()

    match x:
        case "42" | "forty-two" | "forty two":
            return True
         
    


main()

    