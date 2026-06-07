def word_frequency(text):
    """Count how many times each word appears in the text.

    Rules:
    - Split text into words by whitespace
    - Count each word (case-sensitive: 'The' != 'the')
    - Return a dict: {word: count}

    Args:
        text: a string of text

    Returns:
        dict mapping each word to its count

    Example:
        >>> word_frequency('the the cat')
        {'the': 2, 'cat': 1}
    """
    freq = {}
    for word in text.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
