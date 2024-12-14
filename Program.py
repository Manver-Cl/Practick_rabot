# -- coding: cp1251 --
# coding=utf-8

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    """Возвращает список из n простых чисел."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    # Ввод количества простых чисел
    n = int(input("Введите количество простых чисел: "))
    
    # Поиск и вывод простых чисел
    primes = find_primes(n)
    print("Первые", n, "простых чисел:", primes)

if __name__ == "__main__":
    main()
    input("Нажмите Enter, чтобы выйти...")  # Ожидание ввода от пользователя
