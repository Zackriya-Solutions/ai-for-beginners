# AI and Math for Beginners (5-Week Course)

Welcome to the AI and Math for Beginners course! This 5-week program is designed to introduce you to the fundamental mathematical concepts required for AI and machine learning.

## Course Structure

- Week 1: Basic Math Functions in Python
- Week 2: Linear Algebra Basics
- Week 3: Statistics and Probability
- Week 4: Linear Regression
- Week 5: Introduction to Neural Networks

## Prerequisites

- Basic Python programming knowledge
- Familiarity with high school level mathematics

## Setup

1. Fork this repository to your own Github account.
2. Clone your forked repository to your local machine.
3. Install the required packages: pip install -r requirements.txt

## How to Use This Repository

1. Setup the repo
2. For each week's assignment, create a new branch from the main branch.
3. Implement your solutions in the appropriate Python script for the week.
4. Write unit tests for your implementations in the corresponding test file.
5. Commit and push your changes to your forked repository.
6. Create a merge request to the main course repository.
7. Wait for the automated tests to run and review the feedback.
8. Make necessary improvements based on the feedback and update the merge request.

## Weekly Workflow

1. Read the `problem_statement.md` file in the respective week's folder.
2. Implement your solutions in the corresponding Python file (e.g., `basic_math.py` for Week 1).
3. Run the tests using pytest to check your implementation: pytest tests/test_weekX.py
4. Once all tests pass, commit your changes and push to your forked repository.
5. Create a merge request to the main course repository.

## Grading

Your submissions will be graded based on:
1. Correctness of implementation (passing all tests)
2. Code quality and adherence to PEP 8 style guidelines
3. Proper use of comments and docstrings

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [PyTorch Documentation](https://pytorch.org/docs/)


## Submission Guidelines

- All code should be written in Python 3.9 or later.
- Follow PEP 8 style guidelines for your code.
- Include docstrings for all functions and classes.
- Ensure your code passes all tests before submitting.

## Project structure

ai-math-beginners/
│
├── README.md
├── .gitlab-ci.yml
├── requirements.txt
│
├── week1/
│   ├── basic_math.py
│   ├── problem_statement.md
│   └── solution.py
│
├── week2/
│   ├── linear_algebra.py
│   ├── problem_statement.md
│   └── solution.py
│
├── week3/
│   ├── statistics_probability.py
│   ├── problem_statement.md
│   └── solution.py
│
├── week4/
│   ├── linear_regression.py
│   ├── problem_statement.md
│   └── solution.py
│
├── week5/
│   ├── neural_networks.py
│   ├── problem_statement.md
│   └── solution.py
│
└── tests/
    ├── test_week1.py
    ├── test_week2.py
    ├── test_week3.py
    ├── test_week4.py
    └── test_week5.py

Good luck and happy coding!
