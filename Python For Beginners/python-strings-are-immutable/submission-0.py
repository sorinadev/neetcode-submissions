def remove_fourth_character(word: str) -> str:
    first4 = word[:3]
    last_letters = word[4:]
    without_four = first4 + last_letters
    return without_four

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
