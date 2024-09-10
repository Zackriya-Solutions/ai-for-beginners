import numpy as np

def mean(data):
    """
    Calculate the arithmetic mean of a list of numbers.
    
    Args:
    data (list): A list of numbers
    
    Returns:
    float: The arithmetic mean of the data
    
    Raises:
    ValueError: If the input list is empty
    """
    pass

def median(data):
    """
    Calculate the median of a list of numbers.
    
    Args:
    data (list): A list of numbers
    
    Returns:
    float: The median of the data
    
    Raises:
    ValueError: If the input list is empty
    """
    pass

def mode(data):
    """
    Find the mode(s) of a list of numbers.
    
    Args:
    data (list): A list of numbers
    
    Returns:
    list: A list containing the mode(s) of the data
    
    Raises:
    ValueError: If the input list is empty
    """
    pass

def standard_deviation(data):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
    data (list): A list of numbers
    
    Returns:
    float: The standard deviation of the data
    
    Raises:
    ValueError: If the input list has fewer than two elements
    """
    pass

def correlation_coefficient(x, y):
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.
    
    Args:
    x (list): First list of numbers
    y (list): Second list of numbers
    
    Returns:
    float: The Pearson correlation coefficient between x and y
    
    Raises:
    ValueError: If the input lists have different lengths or fewer than two elements
    """
    pass

def binomial_probability(n, k, p):
    """
    Calculate the binomial probability of k successes in n trials with probability p.
    
    Args:
    n (int): Number of trials
    k (int): Number of successes
    p (float): Probability of success on each trial
    
    Returns:
    float: The binomial probability
    
    Raises:
    ValueError: If n or k are negative, or if p is not between 0 and 1
    """
    pass

def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function of a normal distribution.
    
    Args:
    x (float): The point at which to evaluate the PDF
    mean (float): The mean of the normal distribution
    std_dev (float): The standard deviation of the normal distribution
    
    Returns:
    float: The value of the PDF at x
    
    Raises:
    ValueError: If std_dev is not positive
    """
    pass

def bootstrap_mean_ci(data, num_bootstrap_samples, confidence_level):
    """
    (Bonus) Calculate the bootstrap confidence interval for the mean of a dataset.
    
    Args:
    data (list): A list of numbers
    num_bootstrap_samples (int): Number of bootstrap samples to generate
    confidence_level (float): The confidence level (between 0 and 1)
    
    Returns:
    tuple: A tuple containing the lower and upper bounds of the confidence interval
    
    Raises:
    ValueError: If the input list is empty, num_bootstrap_samples is not positive,
                or confidence_level is not between 0 and 1
    """
    pass