# Week 5: Introduction to Neural Networks

## Objective
Implement a basic neural network from scratch using Python and NumPy, and understand the fundamental concepts of neural networks including forward propagation, backpropagation, and gradient descent.

## Tasks

1. Implement a class `NeuralNetwork` with the following methods:
   - `__init__(self, input_size, hidden_size, output_size)`
   - `sigmoid(self, x)`
   - `sigmoid_derivative(self, x)`
   - `forward(self, X)`
   - `backward(self, X, y, output)`
   - `train(self, X, y, epochs, learning_rate)`
   - `predict(self, X)`

2. Create a function `normalize_data(X)` that normalizes the input data.

3. Implement a function `accuracy(y_true, y_pred)` to calculate the accuracy of the model's predictions.

4. Use your implemented neural network to solve a binary classification problem (e.g., classifying points above or below a sine curve).

## Guidelines

- Use NumPy for efficient numerical computations.
- Implement the neural network from scratch without using deep learning libraries like PyTorch or TensorFlow.
- Include proper error handling and input validation.
- Write clear and concise docstrings for each function and method.
- Ensure your code follows PEP 8 style guidelines.

## Bonus Challenge

Extend your neural network to handle multi-class classification problems.

## OKRs (Objectives and Key Results)

- Objective: Gain a fundamental understanding of neural networks and their implementation.
  - KR1: Successfully implement the NeuralNetwork class with all required methods.
  - KR2: Achieve at least 90% accuracy on the binary classification problem.
  - KR3: Pass all unit tests for the implemented functions and methods.
  - KR4: Visualize the decision boundary of the trained neural network.
  - KR5: Complete the bonus challenge by extending the network for multi-class classification.