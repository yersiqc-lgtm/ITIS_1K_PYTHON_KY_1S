def is_prime(n: int) -> bool:
    cont = 0
    for i in range(1,n+1):
        if n%i == 0:
            cont += 1
    return True if cont == 2 else False

def digit_sum(n: str) -> int:
    return sum([int(x) for x in n])

def reverse_number(n: str) -> int:
    record = True if int(n) < 0 else False
    a = -1*int(n) if int(n) < 0 else int(n)
    k = str(a)[::-1]
    return int(k)*-1 if record else int(k)

def max_of_list(numbers: list[int]) -> int | None:
    return max(numbers) if len(numbers) > 0 else None

def count_even(numbers: list[int]) -> list[int | float]:
    return [x for x in numbers if x%2 == 0]

def string_to_list(val: str) -> list[int | float]:
    return list(map(int, val.split()))

def main() -> None:
    print('''
    1 - Простое ли число
    2 - Сумма цифр
    3 - Перевернуть число
    4 - Максимум списка
    5 - Количество чётных
    0 - Выход\n\n
    ''')
    option = int(input("Выберите действие (0 - 5): "))
    num = input("Введите число: ")
    match option:
        case 1: # case num prime
            print("{} - Простое".format(is_prime(int(num))))
        case 2: # case sum digit
            print("Ресультат (+) : {}".format(digit_sum(num)))
        case 3: # case reverse num
            print("Ресультат : {}".format(reverse_number(num)))
        case 4: #list max
            print("Максимум: {}".format(max_of_list(string_to_list(num))))
        case 5: # num of pare
            print("Количество чёеных: {}".format(count_even(string_to_list(num))))



# start program
main()