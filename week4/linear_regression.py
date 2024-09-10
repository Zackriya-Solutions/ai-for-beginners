import numpy as np
import matplotlib.pyplot as plt

def compute_cost(X, y, theta):
    """
    Compute the cost function for linear regression.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    y (numpy.ndarray): Target vector (m x 1)
    theta (numpy.ndarray): Parameter vector (n x 1)
    
    Returns:
    float: The cost
    """
    pass

def gradient_descent(X, y, theta, alpha, num_iters):
    """
    Perform gradient descent to optimize the parameters.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    y (numpy.ndarray): Target vector (m x 1)
    theta (numpy.ndarray): Initial parameter vector (n x 1)
    alpha (float): Learning rate
    num_iters (int): Number of iterations
    
    Returns:
    numpy.ndarray: Optimized parameter vector
    list: History of cost function values
    """
    pass

def normalize_features(X):
    """
    Normalize features to have zero mean and unit variance.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    
    Returns:
    numpy.ndarray: Normalized feature matrix
    numpy.ndarray: Mean of each feature
    numpy.ndarray: Standard deviation of each feature
    """
    pass

def predict(X, theta):
    """
    Make predictions using the learned parameters.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    theta (numpy.ndarray): Parameter vector (n x 1)
    
    Returns:
    numpy.ndarray: Predicted values (m x 1)
    """
    pass

def plot_data_and_line(X, y, theta):
    """
    Visualize the data points and the fitted line.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    y (numpy.ndarray): Target vector (m x 1)
    theta (numpy.ndarray): Parameter vector (n x 1)
    """
    pass

def normal_equation(X, y):
    """
    (Bonus) Compute the optimal parameters using the normal equation method.
    
    Args:
    X (numpy.ndarray): Feature matrix (m x n)
    y (numpy.ndarray): Target vector (m x 1)
    
    Returns:
    numpy.ndarray: Optimal parameter vector
    """
    pass