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
| Classifier                 | Accuracy Score | Recall |
|----------------------------|----------------|--------|
| Logistic Regression        | 0.805195       |  0.90  |
| K-Nearest Neighbors (KNN)  | 0.81168        |  0.93  |      
| Support Vector Classifier  | 0.79870        |  0.89  |
| Gaussian Naive Bayes       | 0.766234       |  0.84
| Decision Tree Classifier   | 0.733766       |  0.76  |
#   Conclusion
The KNN classifier and Logistic Regression achieved the highest accuracy of 81% and an AUC score of 86% but have some small difference in recall score as KNN perform best with 93% where Logistic Regression with 90%. This indicates that the KNN and SVM are well-suited for predicting diabetes based on the features included in our dataset.
