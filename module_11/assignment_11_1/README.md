# Used Car Sales - Price Prediction and Business Impact

## Intro / Context

In this exercise, we analyzed a dataset of used car sales via the CRISP-DM method. The CRISP-DM method stands for Cross-Industry Standard Process for Data Mining and includes the following steps:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

This is a standard approach for developing and deploying data science and/or machine learning solution. Likewise, this method was applied here and is outlined in the notebook found [here](./assignment_11_1_notebook.ipynb). The data source can be found [here](https://mo-pcco.s3.us-east-1.amazonaws.com/BH-PCMLAI/module_11/practical_application_II_starter.zip).

## Setup and Running Jupyter Notebook

To begin, install the required packages provided in the requirements.txt file (preferably in a dedicated environment)

```
pip install -r requirements.txt
```

Then when you open the notebook, add this environment as your kernel. You will have the necessary libraries to run the notebook.

## Summarized Findings and Next Steps

The findings here are included as a summary. For all findings and a full analysis, please see the Conclusions section in the notebook.

Year and odometer seem to have a profound impact on the price of the car. There are a few exceptions such as diesel vehicles, some trucks, etc. These anomalies could be targeted for maximizing revenue/profit. Based on the year and odometer, the company should target newer cars as well as 'classic' cars from the 50's and 60's. In both cases, the lower the odometer the better.
