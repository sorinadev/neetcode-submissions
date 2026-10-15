from typing import List

def read_integers() -> List[int]:
    userinp = input()
    return [int(i) for i in userinp.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
