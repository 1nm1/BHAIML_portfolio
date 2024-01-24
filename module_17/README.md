# Improving Marketing Campaign Efficacy

## Intro / Context

Due to an overwhelming and increasing number of marketing campaigns and economic challenges, marketing organizations are increasingly using alternative approaches to increase impact including more targeted campaigns and the use of Business Intelligence and Data Mining. In this use-case, we are examining data related to targeted marketing campaigns around long-term deposit applications with good interest rates.

Similar to other exercises, the Cross-Industry Standard Process for Data Mining methodology is deployed here and includes the following steps:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

## Documents

You may find the solution notebook [here](./module_17_notebook.ipynb). Images saved during the analysis can be found in the images folder. The included PDF offers a similar analysis to the same dataset and is referenced throughout the analysis conducted here.

## Setup and Running Jupyter Notebook

To begin, install the required packages provided in the requirements.txt file (preferably in a dedicated environment)

```
pip install -r requirements.txt
```

Then when you open the notebook, add this environment as your kernel. You will have the necessary libraries to run the notebook.

## Summarized Findings and Next Steps

Based on these the analysis and findings, we determined that the Decision Tree model performed the best. In expanding on this model and looking at the important inputs to the model, we found the following features to be the most critical:

1. Duration
2. Number of Employees
3. Consumer Confidence Index

With this in mind, we can direct marketing campaigns around groups that exhibit these features or during these times (like months or when indexes hit specific values). This is turn will improve our overall conversion rate into long term deposits and boosts our profits.
