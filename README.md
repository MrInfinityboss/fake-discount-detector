# 🛒 Fake Discount Detector — End-to-End ML + Analytics System

## Overview

Many e-commerce platforms show misleading discounts by artificially inflating the MRP and then applying a large percentage off.
This project detects whether a product discount is **genuine or manipulated** using data analytics and machine learning.

The system analyzes pricing behavior, identifies abnormal discount patterns, trains a fraud detection model, and deploys an interactive dashboard where users can verify deals in real time.

---

## Problem Statement

Customers often trust discounts without realizing:

* The MRP was increased before sale
* The discount percentage is unrealistic
* Reviews do not match pricing behavior

This leads to poor buying decisions.

The goal is to build a system that answers:

> **Is this discount real or fake?**

---

## Solution

The project builds a complete pipeline:

Dataset → Data Cleaning → Pricing Analysis → Fraud Rules → ML Model → Explainability → Live Dashboard

The system generates a prediction based on pricing mismatch and trust signals.

---

## Dataset

Amazon Products Dataset (sampled ~100k records)

Key features used:

* Price
* List Price (MRP)
* Rating
* Number of Reviews

Derived feature:

* Discount Percentage

---

## Fraud Logic (Human Behaviour Based)

Products are considered suspicious if:

* Price > MRP (negative discount)
* Extremely large discount (>80%)
* Pricing inconsistent with trust signals

---

## Machine Learning Model

### Challenge

The dataset had extreme class imbalance:

> Fake deals ≈ 0.1% of data

Accuracy becomes meaningless in such cases.

### Approach

* Created fraud labels based on abnormal pricing behaviour
* Used **SMOTE** to balance rare fraud cases
* Trained **Random Forest Classifier**
* Evaluated using precision & recall instead of accuracy

### Result

The model successfully detects fraudulent discounts while maintaining low false alarms.

---

## Model Explainability

Feature importance analysis shows:

1. Price vs MRP mismatch is the strongest fraud indicator
2. Ratings help validate trust
3. Review count has minimal impact

This confirms real-world shopping behavior patterns.

---

## Live AI Dashboard

An interactive Streamlit application allows users to test any deal.

User inputs:

* Current price
* MRP
* Rating
* Reviews

The model predicts:

> Genuine Deal ✅
> Fake Discount 🚨

This converts the project from analysis → usable product.

---

## Tech Stack

Python
Pandas & NumPy
Scikit-Learn
Imbalanced-Learn (SMOTE)
Matplotlib
Streamlit
Git & GitHub

---

## How to Run Locally

Clone repository

```
git clone https://github.com/MrInfinityboss/fake-discount-detector.git
cd fake-discount-detector/dashboard
```

Install dependencies

```
pip install -r requirements.txt
```

Run dashboard

```
streamlit run app.py
```

---

## Key Learnings

* Fraud detection requires recall optimization, not accuracy
* Class imbalance can mislead ML models
* Explainability is essential for trust
* Data analytics + ML + UI creates real-world impact

---

## Future Improvements

* Price history tracking
* Browser extension for online shopping
* Deep learning anomaly detection
* Real-time API integration

---

## Author

Akshat
Data Analytics & Machine Learning Project
