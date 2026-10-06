def concatenate(s1: str, s2: str) -> str:
    x = s1+s2
    if len(x) <= 10:
        return x
    else:
        return "Too long!"



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
