"""
229.102026
classwork 4
"""

def grade(score):
    if not isinstance(score, (int, float)) or not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return 5
    if score >= 75:
        return 4
    if score >= 60:
        return 3
    return 2
