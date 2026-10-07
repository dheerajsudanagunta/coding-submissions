from typing import List

def contains_duplicate(words: List[str]) -> bool:
    x = set()
    for word in words:
        x.add(word)
    if len(words)==len(x):
        return False
    return True  
    

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
