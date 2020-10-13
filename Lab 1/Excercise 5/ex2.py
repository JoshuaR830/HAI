with open("ex2words.txt", "r") as file:
    lines = file.readlines()

my_list = [line.split() for line in lines]

def convertToInt(list):
    return [list[0].lower(), int(list[1])]

another_list = list(map(convertToInt, my_list))

print(my_list)
print(another_list)