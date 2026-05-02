# Автор: Евгений Чернышов
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # изменена функция: реализовано произведение
    return a * b

def sqrt(x):
    # квадратный корень
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")

