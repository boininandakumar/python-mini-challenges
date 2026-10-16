"""String manipulation challenges."""


def reverse_string(text):
    """Return the text reversed."""
    return text[::-1]


def count_vowels(text):
    """Count the vowels (a, e, i, o, u) in the text, ignoring case."""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def is_palindrome(text):
    """Check if the text reads the same forwards and backwards.

    Only letters and digits are compared, and case is ignored.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sentence = "Python Internship"
    print("Original:", sentence)
    print("Reversed:", reverse_string(sentence))
    print("Vowel count:", count_vowels(sentence))

    for word in ("Madam", "A man a plan a canal Panama", "Python"):
        print(f'"{word}" is a palindrome:', is_palindrome(word))
