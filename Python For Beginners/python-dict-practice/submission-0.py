from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    character_dict = {}
    for letter in word:
        count_value = word.count(letter)
        character_dict[letter] = count_value
    return character_dict



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
