import time
import pytest
from src.hasher import (
    calculate_sha512,
    calculate_sha512_cryptography,
    calculate_sha512_pycryptodome
)


def measure_time(func, data, iterations=10000):
    """Допоміжна функція для вимірювання часу виконання"""
    start = time.perf_counter()
    for _ in range(iterations):
        func(data)
    return time.perf_counter() - start


def test_performance_comparison():
    """Тестовий набір для порівняння швидкодії бібліотек"""
    test_data = "performance_test_string_for_sha512" * 10
    iterations = 10000

    time_hashlib = measure_time(calculate_sha512, test_data, iterations)
    time_crypto = measure_time(calculate_sha512_cryptography, test_data, iterations)
    time_dome = measure_time(calculate_sha512_pycryptodome, test_data, iterations)

    print(f"\n--- Результати продуктивності ({iterations} ітерацій) ---")
    print(f"Стандартна бібліотека (hashlib): {time_hashlib:.4f} сек")
    print(f"Бібліотека Cryptography:          {time_crypto:.4f} сек")
    print(f"Бібліотека PyCryptodome:         {time_dome:.4f} сек")

    assert time_hashlib > 0

