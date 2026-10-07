from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dicts = {}

    for x in word:
        if x in dicts:
            dicts[x] += 1
        else:
            dicts[x] = 1
    return dicts






# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))