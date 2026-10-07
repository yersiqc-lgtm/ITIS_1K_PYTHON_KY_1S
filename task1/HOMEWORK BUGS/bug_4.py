"""программа 4 (уровень 2): yтилиты для списков"""

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

def is_sorted(values: list[int]) -> bool:
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def dedupe(values: list[int], seen=None) -> list[int]:
    if seen is None:
        seen = []
    result = []
    for v in values:
        if v not in seen:
            seen.append(v)
            result.append(v)
    return result

def median(values: list[float]) -> float:
    s = sorted(values)
    if not s:
        raise ValueError("пустой список")
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]

# asserts на граничные случаи
assert merge_sorted([], [1, 2]) == [1, 2]
assert merge_sorted([1, 2], [3, 4]) == [1, 2, 3, 4]
assert is_sorted([]) is True
assert is_sorted([1]) is True
assert is_sorted([1, 1, 2]) is True
assert dedupe([1, 1, 2]) == [1, 2]
assert dedupe([1, 2]) == [1, 2]  # повторный вызов тоже должен работать
assert median([1, 2]) == 1.5
assert median([5, 1, 3]) == 3
