import pytest
import numpy as np
from week3.statistics_probability import (
    mean, median, mode, standard_deviation, correlation_coefficient,
    binomial_probability, normal_pdf, bootstrap_mean_ci
)

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([0, 0, 0, 0]) == 0
    assert abs(mean([1.5, 2.5, 3.5]) - 2.5) < 1e-6
    with pytest.raises(ValueError):
        mean([])

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5, 2, 1, 4, 3]) == 3
    with pytest.raises(ValueError):
        median([])

def test_mode():
    assert mode([1, 2, 2, 3, 3, 3, 4]) == [3]
    assert set(mode([1, 1, 2, 2])) == set([1, 2])
    assert mode([1, 2, 3, 4]) == [1]
    with pytest.raises(ValueError):
        mode([])

def test_standard_deviation():
    assert abs(standard_deviation([1, 2, 3, 4, 5]) - 1.5811388300841898) < 1e-6
    assert standard_deviation([2, 2, 2, 2]) == 0
    with pytest.raises(ValueError):
        standard_deviation([1])

def test_correlation_coefficient():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    assert abs(correlation_coefficient(x, y) - 0.8164965809277261) < 1e-6
    with pytest.raises(ValueError):
        correlation_coefficient([1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        correlation_coefficient([1], [2])

def test_binomial_probability():
    assert abs(binomial_probability(10, 3, 0.5) - 0.1171875) < 1e-6
    assert binomial_probability(5, 0, 0.1) == 0.59049
    with pytest.raises(ValueError):
        binomial_probability(-1, 2, 0.5)
    with pytest.raises(ValueError):
        binomial_probability(10, 3, 1.5)

def test_normal_pdf():
    assert abs(normal_pdf(0, 0, 1) - 0.3989422804014327) < 1e-6
    assert abs(normal_pdf(1, 0, 1) - 0.24197072451914337) < 1e-6
    with pytest.raises(ValueError):
        normal_pdf(0, 0, -1)

def test_bootstrap_mean_ci():
    np.random.seed(42)
    data = [1, 2, 3, 4, 5]
    ci_lower, ci_upper = bootstrap_mean_ci(data, 10000, 0.95)
    assert 2 < ci_lower < ci_upper < 4
    with pytest.raises(ValueError):
        bootstrap_mean_ci([], 1000, 0.95)
    with pytest.raises(ValueError):
        bootstrap_mean_ci([1, 2, 3], 0, 0.95)
    with pytest.raises(ValueError):
        bootstrap_mean_ci([1, 2, 3], 1000, 1.1)