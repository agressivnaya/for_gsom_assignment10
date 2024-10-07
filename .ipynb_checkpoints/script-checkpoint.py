from smallest import find_two_smallest
from integers import (
    positive_numbers,
    negative_numbers,
    mixed_numbers,
    even_numbers,
    random_numbers
)

# List of lists to process
lists_to_process = [
    positive_numbers,
    negative_numbers,
    mixed_numbers,
    even_numbers,
    random_numbers
]

# Open the result.txt file to write results
with open('result.txt', 'w') as result_file:
    for numbers in lists_to_process:
        smallest_values = find_two_smallest(numbers)
        result_file.write(f"{numbers}: {smallest_values}\n")

print("Results have been saved to result.txt.")