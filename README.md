# Diabetes-prediction-using-various-ML_Algorithms

# Introduction
This report evaluates the performance of a diabetes prediction model using various classifiers.

#  Exploratory Analysis
The dataset included 7 predictor variables: Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. Key observations from exploratory analysis:

No duplicates were found in the dataset.
Outliers were detected and capped to minimize their impact on the analysis.
Initially, there were no NaN (missing) values observed in the dataset. However, zeros were identified in certain features, which were treated as missing values. These zeros were replaced with NaN values, and missing data imputation techniques were applied later in the analysis.
#  Classifier Scores
Classifier	Score
|       Classifier           | Accuracy Score | Recall of   positive class   |  f1 score (Positive class)       |                                            
|----------------------------|----------------|-------- -------------------   |---------------------------------|
| Logistic Regression        | 0.805195       |  0.60                         |   0.65                         |
| K-Nearest Neighbors (KNN)  | 0.81168        |  0.57                         |   0.66                         |
| Support Vector Classifier  | 0.79870        |  0.60                         |   0.64                         |
| Gaussian Naive Bayes       | 0.766234       |  0.60                         |   0.61                         |
| Decision Tree Classifier   | 0.733766       |  0.68                         |   0.61                         |
#   Conclusion
The KNN classifier and Logistic Regression achieved the highest accuracy of 81% and an AUC score of 86% . We are doing diabetes where recall and f1 score have more importance .Logistic Regression and Decision Tree classifier have good recall and f1 score.erall ,Logistic regression is performing best in term of recall(more focussed),f1_score and accuracy.
