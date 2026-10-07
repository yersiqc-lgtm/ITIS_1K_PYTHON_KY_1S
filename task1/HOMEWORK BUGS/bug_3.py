"""программа 3: Температура за неделю"""

def count_above(values: list[int], limit: int) -> int:
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count

def max_streak(values: list[int], limit: int) -> int:
    best = 0
    current = 0
    for v in values:
        if v > limit:
            current += 1
        else:
            if current > best:
                best = current
            current = 0
    if current > best:
        best = current
    return best

def average(values: list[int]) -> float:
    return sum(values) / len(values)

def main() -> None:
    temps = [12, 18, 21, 19, 14, 22, 25, 23]
    print(count_above(temps, 20))
    print(max_streak(temps, 20))
    print(average(temps))

if __name__ == "__main__":
    main()
