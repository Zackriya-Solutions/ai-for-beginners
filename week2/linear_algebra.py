import numpy as np

def vector_add(v1, v2):
    """
    Add two vectors.
    
    Args:
    v1 (numpy.ndarray): First vector
    v2 (numpy.ndarray): Second vector
    
    Returns:
    numpy.ndarray: The sum of v1 and v2
    
    Raises:
    ValueError: If v1 and v2 have different dimensions
    """
    pass

def scalar_multiply(c, v):
    """
    Multiply a vector by a scalar.
    
    Args:
    c (float): Scalar value
    v (numpy.ndarray): Vector
    
    Returns:
    numpy.ndarray: The result of c * v
    """
    pass

def dot_product(v1, v2):
    """
    Calculate the dot product of two vectors.
    
    Args:
    v1 (numpy.ndarray): First vector
    v2 (numpy.ndarray): Second vector
    
    Returns:
    float: The dot product of v1 and v2
    
    Raises:
    ValueError: If v1 and v2 have different dimensions
    """
    pass

def matrix_multiply(m1, m2):
    """
    Multiply two matrices.
    
    Args:
    m1 (numpy.ndarray): First matrix
    m2 (numpy.ndarray): Second matrix
    
    Returns:
    numpy.ndarray: The product of m1 and m2
    
    Raises:
    ValueError: If the matrices have incompatible dimensions for multiplication
    """
    pass

def transpose(matrix):
    """
    Calculate the transpose of a matrix.
    
    Args:
    matrix (numpy.ndarray): Input matrix
    
    Returns:
    numpy.ndarray: The transpose of the input matrix
    """
    pass

def is_orthogonal(matrix):
    """
    Check if a matrix is orthogonal.
    
    Args:
    matrix (numpy.ndarray): Input matrix
    
    Returns:
    bool: True if the matrix is orthogonal, False otherwise
    
    Raises:
    ValueError: If the input is not a square matrix
    """
    pass

def eigenvalues(matrix):
    """
    (Bonus) Calculate the eigenvalues of a 2x2 or 3x3 matrix.
    
    Args:
    matrix (numpy.ndarray): Input matrix (2x2 or 3x3)
    
    Returns:
    numpy.ndarray: Array of eigenvalues
    
    Raises:
    ValueError: If the input is not a 2x2 or 3x3 matrix
    """
    pass