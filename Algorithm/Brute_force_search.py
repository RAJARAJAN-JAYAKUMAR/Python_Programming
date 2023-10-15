def brute_force_search(text, pattern):
    """
    Brute-Force Search Algorithm to find all occurrences of 'pattern' in 'text'.

    :param text: The text to search within.
    :param pattern: The pattern to search for.
    :return: A list of starting positions of 'pattern' in 'text'.
    """
    occurrences = []

    text_length = len(text)
    pattern_length = len(pattern)

    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences

# Example usage:
text = "RAJARAJAN"
pattern = "RAJ"
result = brute_force_search(text, pattern)
print("Pattern found at positions:", result)

# x = 2
# y = 3

# x + y -1
