''''[LEARNING LOGS] Colors'''

co = input()
lor = input()

if (co == "Red" and lor == "Yellow") or (co == "Yellow" and lor == "Red"):
    print("Orange")
elif (co == "Red" and lor == "Red"):
    print("Red")
elif (co == "Yellow" and lor == "Yellow"):
    print("Yellow")
elif (co == "Blue" and lor == "Blue"):
    print("Blue")
elif (co == "Yellow" and lor == "Blue") or (co == "Blue" and lor == "Yellow"):
    print("Green")
elif (co == "Red" and lor == "Blue") or (co == "Blue" and lor == "Red"):
    print("Violet")
else:
    print("Error")
