import numpy as np
import pytest
from week5.neural_networks import NeuralNetwork, normalize_data, accuracy, generate_sine_data

def test_neural_network_initialization():
    nn = NeuralNetwork(2, 3, 1)
    assert nn.W1.shape == (2, 3)
    assert nn.b1.shape == (1, 3)
    assert nn.W2.shape == (3, 1)
    assert nn.b2.shape == (1, 1)

def test_sigmoid():
    nn = NeuralNetwork(2, 3, 1)
    x = np.array([-1, 0, 1])
    expected = np.array([0.26894142, 0.5, 0.73105858])
    np.testing.assert_almost_equal(nn.sigmoid(x), expected, decimal=6)

def test_sigmoid_derivative():
    nn = NeuralNetwork(2, 3, 1)
    x = np.array([0.25, 0.5, 0.75])
    expected = np.array([0.1875, 0.25, 0.1875])
    np.testing.assert_almost_equal(nn.sigmoid_derivative(x), expected, decimal=6)

def test_forward_propagation():
    nn = NeuralNetwork(2, 3, 1)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    output = nn.forward(X)
    assert output.shape == (4, 1)
    assert np.all((output >= 0) & (output <= 1))

def test_train_and_predict():
    np.random.seed(42)
    X, y = generate_sine_data(1000)
    X_normalized = normalize_data(X)
    nn = NeuralNetwork(2, 5, 1)
    nn.train(X_normalized, y, epochs=1000, learning_rate=0.1)
    y_pred = nn.predict(X_normalized)
    assert accuracy(y, y_pred) > 0.9

def test_normalize_data():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    X_norm = normalize_data(X)
    assert X_norm.min() == 0
    assert X_norm.max() == 1

def test_accuracy():
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0.1, 0.9, 0.8, 0.3, 0.6])
    assert accuracy(y_true, y_pred) == 0.8

def test_generate_sine_data():
    X, y = generate_sine_data(1000)
    assert X.shape == (1000, 2)
    assert y.shape == (1000, 1)
    assert np.all((y == 0) | (y == 1))