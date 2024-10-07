def find_two_smallest(numbers):
    
    if len(numbers) < 2:
        return None #Not enough elements to find two smallest

    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in numbers:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number
            
    return (smallest, second_smallest)