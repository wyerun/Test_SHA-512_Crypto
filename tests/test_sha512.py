import pytest
from src.hasher import (
    calculate_sha512,
    calculate_sha512_cryptography,
    calculate_sha512_pycryptodome
)


@pytest.mark.parametrize("test_input", ["hello", "cybersecurity", "variant7"])
def test_cross_library_verification(test_input):
    """Перевірка, що всі три бібліотеки видають ідентичний хеш"""
    res1 = calculate_sha512(test_input)
    res2 = calculate_sha512_cryptography(test_input)
    res3 = calculate_sha512_pycryptodome(test_input)

    assert res1 == res2 == res3
    print(f"\n[OK] All libraries matched for: {test_input}")