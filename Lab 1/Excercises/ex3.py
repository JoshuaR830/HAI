myString = "Hello"

try:
    print(myString[-len(myString) - 1])
    print("It can't go too far left")
except IndexError:
    print("It can go too far left")