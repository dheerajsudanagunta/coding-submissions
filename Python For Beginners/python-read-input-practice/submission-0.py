def add_two_numbers() -> int:
    x = input()
    add = x.split(",")
    z = 0
    for i in add:
        z += int(i)
    return z



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
