import pytest
import numpy as np
from week2.linear_algebra import vector_add, scalar_multiply, dot_product, matrix_multiply, transpose, is_orthogonal, eigenvalues

def test_vector_add():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    assert np.array_equal(vector_add(v1, v2), np.array([5, 7, 9]))
    
    with pytest.raises(ValueError):
        vector_add(np.array([1, 2]), np.array([1, 2, 3]))

def test_scalar_multiply():
    v = np.array([1, 2, 3])
    assert np.array_equal(scalar_multiply(2, v), np.array([2, 4, 6]))

def test_dot_product():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    assert dot_product(v1, v2) == 32
    
    with pytest.raises(ValueError):
        dot_product(np.array([1, 2]), np.array([1, 2, 3]))

def test_matrix_multiply():
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    result = np.array([[19, 22], [43, 50]])
    assert np.array_equal(matrix_multiply(m1, m2), result)
    
    with pytest.raises(ValueError):
        matrix_multiply(np.array([[1, 2], [3, 4]]), np.array([[1, 2, 3], [4, 5, 6]]))

def test_transpose():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    result = np.array([[1, 4], [2, 5], [3, 6]])
    assert np.array_equal(transpose(m), result)

def test_is_orthogonal():
    orthogonal = np.array([[0, 1], [-1, 0]])
    not_orthogonal = np.array([[1, 1], [1, 1]])
    
    assert is_orthogonal(orthogonal) == True
    assert is_orthogonal(not_orthogonal) == False
    
    with pytest.raises(ValueError):
        is_orthogonal(np.array([[1, 2, 3], [4, 5, 6]]))

def test_eigenvalues():
    m1 = np.array([[1, 2], [2, 1]])
    m2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    assert np.allclose(eigenvalues(m1), np.array([3, -1]))
    assert np.allclose(sorted(eigenvalues(m2)), sorted(np.array([16.11684397, -1.11684397, 0])))
    
    with pytest.raises(ValueError):
        eigenvalues(np.array([[1, 2, 3], [4, 5, 6]]))