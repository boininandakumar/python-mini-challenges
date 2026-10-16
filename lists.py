"""List operation challenges."""


def find_largest_smallest(numbers):
    """Return (largest, smallest) of a list, or (None, None) if it is empty."""
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest, smallest


def remove_duplicates(items):
    """Return a new list without duplicates, keeping the original order."""
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def common_elements(list_a, list_b):
    """Return the elements that appear in both lists (no repeats)."""
    common = []
    for item in list_a:
        if item in list_b and item not in common:
            common.append(item)
    return common


if __name__ == "__main__":
    numbers = [4, 7, 2, 7, 9, 2]
    largest, smallest = find_largest_smallest(numbers)
    print("Numbers:", numbers)
    print("Largest:", largest, "| Smallest:", smallest)
    print("Without duplicates:", remove_duplicates(numbers))

    first = [1, 2, 3, 4, 5]
    second = [4, 5, 6, 7]
    print("Common elements:", common_elements(first, second))
