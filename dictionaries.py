"""Dictionary challenges."""


def char_frequency(text):
    """Count how many times each character appears in the text."""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def merge_dicts(first, second):
    """Return a new dictionary with both inputs merged (second wins on clashes)."""
    merged = first.copy()
    merged.update(second)
    return merged


def key_with_max_value(data):
    """Return the key that has the highest value, or None if empty."""
    best_key = None
    for key, value in data.items():
        if best_key is None or value > data[best_key]:
            best_key = key
    return best_key


if __name__ == "__main__":
    print("Frequency of 'banana':", char_frequency("banana"))

    dict_a = {"a": 1, "b": 2}
    dict_b = {"b": 3, "c": 4}
    print("Merged:", merge_dicts(dict_a, dict_b))

    marks = {"Nandu": 85, "Gopal": 90, "Ravi": 80}
    print("Top scorer:", key_with_max_value(marks))
    print("Average marks:", sum(marks.values()) / len(marks))
