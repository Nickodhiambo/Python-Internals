#!/usr/bin/env python

def get_lucky_number(name: str)-> int:
    splitted_names = name.split(' ')
    first_name, second_name = splitted_names[0],\
            splitted_names[1]

    vowel_count_name_one = 0
    cons_count_name_one = 0
    vowel_count_name_two = 0
    cons_count_name_two = 0

    vowels = 'aeiou'

    for ch in first_name:
        if ch in vowels:
            vowel_count_name_one +=1
        else:
            cons_count_name_one += 1

    for ch in second_name:
        if ch in vowels:
            vowel_count_name_two += 1
        else:
            cons_count_name_two += 1

    min_product = min(len(first_name), len(second_name))*min(vowel_count_name_one, vowel_count_name_two)*min(cons_count_name_one, cons_count_name_two)

    max_product = max(len(first_name), len(second_name))*max(vowel_count_name_one, vowel_count_name_two)*max(cons_count_name_one, cons_count_name_two)

    lucky_number = max_product - min_product
    if lucky_number == 0:
        return 13
    else:
        return lucky_number
