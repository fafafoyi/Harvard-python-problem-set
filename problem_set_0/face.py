def main():

    out = conver(input())

    print(out)
    return

def conver(text: str):

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    
    return text


main()
