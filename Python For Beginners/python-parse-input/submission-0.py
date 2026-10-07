from typing import List

def read_integers() -> List[int]:
    x = input()
    z = x.split(",")
    lists = []
    for i in z:
        lists.append(int(i))
    return lists


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
