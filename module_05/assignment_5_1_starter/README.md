# README for Assignment 5.1: Will the Customer Accept the Coupon?

## Directory Structure

```
| module_5
 └─ assignment_5_1_starter
  └─ 5.1_charts: images generated from the prompt_nmeek notebook
  └─ data: data used for this assignment
  └─ images: images used for this assignment
  └─ prompt_nmeek.ipynb: the completed notebook for this assignment
  └─ prompt.ipynb: the template notebook for this assignment
README.md: this file

```

## Getting Started

- To start, open the notebook titled prompt_nmeek.ipynb

## Summary of Findings:

Based on the charts and the feature importance, I would say that the most important factors for coupon acceptance are:

1. The type of coupon (in this case if it's carry out or not)
2. The type of establishment (cheap restaurant, coffee house, etc)
3. The expiration date of the coupon (1 day tends to be more popular than 2 days)
4. The temperature (the hotter it is, the more likely a coupon will be accepted)
5. The frequency of visits to a particular establishment
6. Attributes of the individual (age, education, income, etc)

Likewise, the factors that tend to led to rejected coupons are:

1. The type of coupon and/or establishment (bar)
2. Expiration date (if it expires in the next couple of hours)
3. If the weather conditions make it difficult to use the coupon
4. How frequent someone visits an establishment (or lack thereof)
5. Attributes, in this case mostly lower income with kids or widowed tend to not use coupons
