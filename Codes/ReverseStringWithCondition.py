def reverse_string_with_condition(input_str):
    reversed_str = ""
    found_hash = False

    for char in input_str:
        if char == '#':
            found_hash = not found_hash
        elif found_hash:
            reversed_str = char + reversed_str

    return reversed_str


original_str = "Hello, #World!# This is a test."
reversed_str = reverse_string_with_condition(original_str)
print(reversed_str)
