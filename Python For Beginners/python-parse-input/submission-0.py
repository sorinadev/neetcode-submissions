from typing import List

def read_integers() -> List[int]:
    line = input()
    line_list = line.split(",")
    int_line_list = []
    for i in line_list:
        int_line_list.append(int(i))
    return int_line_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
