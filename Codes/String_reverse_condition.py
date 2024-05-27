# String = #abc*defg&hijk --- Output : after even = not reverse , after odd == reverse
# # -- 0 , * - 4 (4-0) = 4

def alternate_reverse_special_substrings(input_str):
    result = []
    current_substring = []
    reverse_flag = False
    special_chars = []

    for char in input_str:
        if char.isalnum():
            current_substring.append(char)
        else:
            special_chars.append(char)
            if reverse_flag:
                result.extend(reversed(current_substring))
            else:
                result.extend(current_substring)

            current_substring = []
            reverse_flag = not reverse_flag

    # Append the remaining characters if any
    if reverse_flag:
        result.extend(reversed(current_substring))
    else:
        result.extend(current_substring)

    # Insert special characters at their original positions
    for special_char in special_chars:
        result.insert(input_str.index(special_char), special_char)

    return ''.join(result)  # It will return string 
    #return result --- It will return list 

# Example usage:
input_string = "#abc*defg&hijk"
output_string = alternate_reverse_special_substrings(input_string)
print(output_string)
