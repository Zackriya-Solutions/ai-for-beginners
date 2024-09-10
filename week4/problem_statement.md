# Week 4: Linear Regression

## Objective
Implement linear regression from scratch and use it to analyze and predict data. This week will bridge the gap between basic mathematics and machine learning concepts.

## Tasks

1. Implement a function `compute_cost(X, y, theta)` that calculates the cost function for linear regression.
2. Create a function `gradient_descent(X, y, theta, alpha, num_iters)` that performs gradient descent to optimize the parameters.
3. Implement a function `normalize_features(X)` that normalizes the features to have zero mean and unit variance.
4. Write a function `predict(X, theta)` that makes predictions using the learned parameters.
5. Create a function `plot_data_and_line(X, y, theta)` that visualizes the data points and the fitted line.

## Guidelines

- Use NumPy for efficient numerical computations.
- Implement the algorithms from scratch without using scikit-learn or other ML libraries.
- Include proper error handling and input validation.
- Write clear and concise docstrings for each function.
- Ensure your code follows PEP 8 style guidelines.

## Bonus Challenge

Implement a function `normal_equation(X, y)` that computes the optimal parameters using the normal equation method.

## Dataset

Use the provided `housing_prices.csv` dataset, which contains information about housing prices based on various features. The goal is to predict the price of a house given its features.

## OKRs (Objectives and Key Results)

- Objective: Gain a deep understanding of linear regression and its implementation.
  - KR1: Successfully implement all 5 required functions.
  - KR2: Achieve a mean squared error (MSE) of less than 25 on the test set.
  - KR3: Visualize the data and the fitted line with proper labels and title.
  - KR4: Write a brief report (max 500 words) explaining your implementation and results.
  - KR5: Complete the bonus challenge function and compare its results with gradient descent.