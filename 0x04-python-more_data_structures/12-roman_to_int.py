def roman_to_int(roman_string: str) -> int:
    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for i in range(len(roman_string) - 1, -1, -1):
        curr_value = roman_to_int_dict[roman_string[i]]
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value
    return result
