def add_two_numbers() -> int:
    user_in = input()
    string_list = user_in.split(",")
    sum_of_input = 0
    for i in string_list:
        sum_of_input += int(i)
    

    return sum_of_input
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
