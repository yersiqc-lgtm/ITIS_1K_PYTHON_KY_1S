"""
29.10.2026
classwork 3
"""

def discount(price, percent):
    return price - price * percent / 100

def total(prices):
    s = 0
    for i in range(len(prices)):
        s += prices[i]
    return s

def is_adult(age):
    return age >= 18

def last_word(text):
    words = text.split()
    return words[-1] if words else ""
