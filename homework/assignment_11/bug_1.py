""" программа 1: Оценки группы"""

def to_grade(score: int) -> str:
    if score >= 86:
        return "отлично"
    elif score >= 71:
        return "хорошо"
    elif score >= 56:
        return "удовлетворительно"
    else:
        return "неудовлетворительно"

def count_grades(scores: list[int]) -> dict[str, int]:
    counts = {}
    for s in scores:
        grade = to_grade(s)
        counts[grade] = counts.get(grade, 0) + 1
    return counts

def main() -> None:
    raw = input("Баллы через пробел: ")
    scores = [int(x) for x in raw.split()]
    print(count_grades(scores))
    print("Средний балл:", sum(scores) / len(scores))

if __name__ == "__main__":
    main()
