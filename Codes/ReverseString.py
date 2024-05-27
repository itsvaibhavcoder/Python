#Using Slicing
'''
def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

# Example usage:
original_str = "Hello, World!"
reversed_str = reverse_string(original_str)
print(reversed_str)

'''
#Using loop

def reverse(input):
    reversed = ""
    for char in input:
        reversed = char + reversed
    return reversed

original_str = "Hello, World!"
reversed_str = reverse(original_str)
print(reversed_str)
