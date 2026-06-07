def placement_fizzbuzz(n):
    """Return a FizzBuzz-style list adapted for placement prep.

    For each number from 1 to n:
    - If divisible by both 3 and 5: "PlacementReady"
    - If divisible by 3 only: "Placement"
    - If divisible by 5 only: "Ready"
    - Otherwise: the number as a string

    Args:
        n: positive integer

    Returns:
        list of strings

    Examples:
        >>> placement_fizzbuzz(5)
        ['1', '2', 'Placement', '4', 'Ready']
    """
    result = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            result.append("PlacementReady")
        elif num % 3 == 0:
            result.append("Placement")
        elif num % 5 == 0:
            result.append("Ready")
        else:
            result.append(str(num))
    return result
