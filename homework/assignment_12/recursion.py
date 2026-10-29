"""
29.10.2026
homework
"""

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' -> nonnegative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' -> nonnegative integer")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_fast(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' -> nonnegative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def to_binary(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("'n' -> nonnegative integer")
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

def hanoi(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("'n' -> positive integer")
    moves = []

    def move(count, source, target, auxiliary):
        if count == 0:
            return
        move(count - 1, source, auxiliary, target)
        moves.append((source, target))
        move(count - 1, auxiliary, target, source)

    move(n, "A", "C", "B")
    return moves

if __name__ == "__main__":
    pass