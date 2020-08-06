# 2020-mlb-eda-project

## This branch is strictly for Research

#### What Kind of Models can we choose from?

- SVM
- Linear Regression
- Logistical Regression
- Linear Discriminant Analysis
- Decision Tree
- K-nearest neighbor
- Neural Networks(Multi-layer perceptron)
- Similarity Learning

- The risk R(g) of function g is defined as the expected loss of g. This can be estimated from the training data as

#### ![risk equation](./images/risk.svg 'Risk Equation')

- The supervised learning optimization problem is to find the function g that minimizes

#### ![optimize equation](./images/optimize.svg 'Optimize Equation')

All information above came from [Here](https://en.wikipedia.org/wiki/Supervised_learning)

#### What performance measurments can we make on our models?

- Cornell Performance Measures [Study](https://www.cs.cornell.edu/courses/cs578/2003fa/performance_measures.pdf)

##### Most common preformance measurements:

- Accuracy
- Weighted (Cost Sensitive) Accuracy
- Lift
- Precision/Recall
  - F Score
  - Break Even Point
- ROC
  - ROC Area

##### Accuracy

- Target: 0/1, -1/+1, True/False, etc
- Prediction = f(inputs) = f(x): 0/1 or Real
- Threshold: f(x) > thresh => 1, else => 0
  - threshold(f(x)): 0/1
- correct / total
- p(correct): p(threshold(f(x)) = target)

- Problems with accuracy:
  - Assumes equal for both kinds of errors
  - is 99% accuracy good?
    - can be many different things(excellent, good, mediocre, poor, terrible)
    - depends on problem
  - is 10% accuracy bad?
    - information retrieval
  - BaseRate = accuracy of predicting predominant class
