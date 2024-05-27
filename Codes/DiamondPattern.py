def print_diamond(rows):
    for i in range(0, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        
        # Print stars (left half of the diamond)
        print("* " * i)

    for i in range(rows - 1, 0, -1):
        # Print spaces
        print(" " * (rows - i), end="")

        # Print stars (right half of the diamond)
        print("* " * i)

# Example usage:
num_rows = 5
print_diamond(num_rows)
