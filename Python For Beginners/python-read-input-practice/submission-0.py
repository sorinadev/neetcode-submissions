def add_two_numbers() -> int:
    user_in = input()
    string_list = user_in.split(",")
    int_user_list = []
    sum_of_input = 0
    for i in string_list:
        int_user_list.append(int(i))
    for i in int_user_list:
        sum_of_input += i

    return sum_of_input
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
