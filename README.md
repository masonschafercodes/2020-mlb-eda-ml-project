# 2020-mlb-eda-project

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

  - Percent Reduction in Error

    - 8% accuracy = 20% error
    - if learning increases accuracy to 90% that means we drop from 20% E to 10% E
    - Thats a 50% reduction in error

#### Lift

- We are not interested in the accuracy on the entire dataset
- want accurate predictions for 5%, 10% or 20% of the data set
- dont care about the remaining
- one typical application would be in marketing
- how much better than random prediction on the fraction of the dataset predicted true (f(x) > threshold)
- Lift and Accuracy do not always correlate well

#### Precision and Recall

- Precision:
  - how many of the returned documents are correct
  - precision(threshold)
- Recall:
  - how many of the positives does the model return
  - recall(threshold)

#### ROC Plot and ROC Area

- Reciever Operator Characteristic
- Developed in WWII to statistically model false positives and false negatives detections of radar operators
- Better statistical foundations than most other measures
- Standard measure in medicine and biology
- Becoming more popular in ML

#### ROC Plot

- Measures Sweep threshold and plot

  - TPR vs. FPR
  - Sensitivity vs 1-Specificity
  - P(true|true) vs P(true|false)

- Properties of ROC:
  - 1.0: perfect prediction
  - 0.9: excellent prediction
  - 0.8: good prediction
  - 0.7: mediocre prediction
  - 0.6: poor prediction
  - 0.5: random prediction
  - <0.5: something wrong!

#### Summary of Metrics

- the measure you optimize to makes a difference
- the measure you report makes a difference
- use measure appropriate for problem/community
- accuracy often is not sufficient/appropriate
- ROC is gaining popularity in the ML community
- only accuracy generalizes to >2 classes!
