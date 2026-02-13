# 🛒 Fake Discount Detector

Detects whether an e-commerce discount is genuine or manipulated using real product pricing data.

---

## Problem

Many online stores artificially increase the MRP and then show large discounts.
This misleads customers into believing they are getting a deal.

---

## Solution

This project analyzes product pricing data and calculates a **Deal Authenticity Score (0–100)** based on:

* Actual price vs listed price
* Discount percentage anomalies
* Product rating reliability
* Review count trustworthiness

---

## Features

* Detect fake pricing (price > MRP)
* Detect suspicious high discounts (>80%)
* Generate authenticity score for each product
* Identify best genuine deals
* Identify scam-like products

---

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn

---

## Example Output

Top genuine deals and suspicious products are automatically identified using the scoring algorithm.

---

## Future Improvements

* Machine learning classification model
* Brand-level trust ranking
* Price history tracking
* Power BI dashboard
