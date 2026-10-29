""" программа 2: Список покупок"""

def find_index(items: list[str], target: str) -> int:
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def remove_all(items: list[str], target: str) -> list[str]:
    result = []
    for item in items:
        if item != target:
            result.append(item)
    return result

def get_last(items: list[str], n: int) -> list[str]:
    return items[-n:]

def main() -> None:
    shopping = ["хлеб", "молоко", "сыр", "молоко", "яблоки"]
    print(find_index(shopping, "сыр"))
    print(find_index(shopping, "кефир"))
    print(remove_all(shopping, "молоко"))
    print(get_last(shopping, 2))
    print("Всего: " + str(len(shopping)) + " товаров")

if __name__ == "__main__":
    main()
