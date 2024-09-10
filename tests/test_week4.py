import pytest
import numpy as np
from week4.linear_regression import compute_cost, gradient_descent, normalize_features, predict, normal_equation

def test_compute_cost():
    X = np.array([[1, 1], [1, 2], [1, 3]])
    y = np.array([1, 2, 3])
    theta = np.array([0, 1])
    assert np.isclose(compute_cost(X, y, theta), 0.0)

def test_gradient_descent():
    X = np.array([[1, 1], [1, 2], [1, 3]])
    y = np.array([1, 2, 3])
    theta = np.array([0, 0])
    alpha = 0.01
    num_iters = 1000
    theta, _ = gradient_descent(X, y, theta, alpha, num_iters)
    assert np.allclose(theta, [0, 1], atol=1e-2)

def test_normalize_features():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    X_norm, mean, std = normalize_features(X)
    assert np.allclose(np.mean(X_norm, axis=0), [0, 0], atol=1e-6)
    assert np.allclose(np.std(X_norm, axis=0), [1, 1], atol=1e-6)

def test_predict():
    X = np.array([[1, 1], [1, 2], [1, 3]])
    theta = np.array([1, 1])
    predictions = predict(X, theta)
    assert np.allclose(predictions, [2, 3, 4])

def test_normal_equation():
    X = np.array([[1, 1], [1, 2], [1, 3]])
    y = np.array([1, 2, 3])
    theta = normal_equation(X, y)
    assert np.allclose(theta, [0, 1], atol=1e-6)