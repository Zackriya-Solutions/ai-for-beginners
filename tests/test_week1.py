import pytest
from week1.basic_math import factorial, fibonacci, is_prime, gcd, lcm, prime_factors

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    with pytest.raises(ValueError):
        fibonacci(0)

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(100) == False
    with pytest.raises(ValueError):
        is_prime(1)

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(100, 75) == 25
    assert gcd(3, 7) == 1
    with pytest.raises(ValueError):
        gcd(0, 5)

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(8, 9) == 72
    with pytest.raises(ValueError):
        lcm(0, 5)

def test_prime_factors():
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(100) == [2, 2, 5, 5]
    assert prime_factors(17) == [17]
    with pytest.raises(ValueError):
        prime_factors(1)