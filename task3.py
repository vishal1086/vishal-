while (True):

    name = input("enter your name").strip()
    length = len(name)
    if length>20:
        print("username cannot be more than 20 letters in length")

    elif length==1:
        print("Sorry username must be longer than one letter")

    elif (length<20):
        print("thank you")

        break



