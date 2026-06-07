def gradebook_stats(gradebook):
    """Analyze a gradebook dictionary.

    Args:
        gradebook: dict mapping student_name (str) -> list of numeric grades

    Returns:
        dict mapping student_name -> dict with:
            "average": float rounded to 2 decimal places
            "highest": max grade (int or float)
            "lowest": min grade (int or float)

    Example:
        >>> gradebook_stats({"Alice": [90, 85, 92]})
        {'Alice': {'average': 89.0, 'highest': 92, 'lowest': 85}}
    """
    stats = {}
    for student, grades in gradebook.items():
        stats[student] = {
            "average": round(sum(grades) / len(grades), 2),
            "highest": max(grades),
            "lowest": min(grades),
        }
    return stats
