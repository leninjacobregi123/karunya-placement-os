def count_eligible(scores, cutoff):
    """Return how many scores are >= cutoff.

    Do not use built-in filtering helpers; practice loops and conditions.

    Args:
        scores: list of integers
        cutoff: integer threshold

    Returns:
        int: count of eligible scores
    """
    count = 0
    for score in scores:
        if score >= cutoff:
            count += 1
    return count
