import pytest
import time
from src.hasher import calculate_sha512


def test_performance_large_payload():
    """Тест продуктивності: обробка 10 МБ даних"""
    # Генеруємо великий рядок (приблизно 10 МБ)
    payload = "A" * 10_000_000

    start_time = time.time()
    result = calculate_sha512(payload)
    end_time = time.time()

    duration = end_time - start_time

    # Виводимо результат у лог (видимо через pytest -s)
    print(f"\n[Performance] SHA-512 processed 10MB in: {duration:.4f}s")

    # Перевіряємо, чи результат не порожній
    assert result is not None
    # Встановлюємо поріг (наприклад, не довше 0.5 секунди)
    assert duration < 0.5


def test_reproducibility_under_load():
    """Перевірка стабільності обчислень при багаторазовому запуску"""
    payload = "performance_test_data"
    results = set()

    for _ in range(100):
        results.add(calculate_sha512(payload))

    # Якщо набір містить лише 1 елемент, значить обчислення стабільні
    assert len(results) == 1