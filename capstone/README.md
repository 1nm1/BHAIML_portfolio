# Agricultural Yield Prediction From Environmental Factors

Prepared by Nathan Meek (Q1 2024)

## Executive summary

The escalating impact of climate change poses a significant threat to global food security. This analysis and report aim to model agricultural yields based on environmental factors that are becoming increasingly unpredictable due to climate change. Utilizing data from the Food and Agriculture Organization of the United Nations (FAOSTAT) and the World Bank Group Climate Change Portal and following the CRISP-DM methodology, this study focuses on regression models to predict crop yields under various climate scenarios. This approach facilitates informed decision-making regarding crop selection, irrigation practices, and resource allocation to mitigate the adverse effects of climate change on agriculture.

Key findings indicate that crop type, pesticide use, temporal factors related to climate phenomena, and critical growth period conditions (temperature and rainfall) significantly influence agricultural yield. Root crops and increased pesticide usage are notably associated with higher yields, while temperature fluctuations and rainfall impact crop growth. The study emphasizes the importance of selecting resilient crops and utilizing pesticides efficiently, alongside the need for international collaboration and sustainable agricultural technologies to enhance food security in the face of climate change.

## Research Question

Can we model agricultural yield based on environmental factors especially as become more unpredictable due to climate change?

## Rationale

As the world continues to warm through climate change, food available and security is increasingly at risk. Understanding the expected yields for certain products in various regions of the world can give insight into where food scarcity might become a pressing issue in the future. This understanding is critical for planning and implementing strategies to mitigate the impact of climate change on agriculture.

Predictive models can be developed to forecast crop yields under different climate scenarios, allowing policymakers and farmers to make informed decisions about crop selection, irrigation practices, and resource allocation. International cooperation and investment in sustainable agricultural technologies will be essential to enhance food security globally, especially in areas most susceptible to the adverse effects of climate change.

## Data Sources

- [Food and Agriculture Organization of the United Nations (FAOSTAT)](https://www.fao.org/faostat/en/#data)

- [World Bank Group Climate Change Portal](https://climateknowledgeportal.worldbank.org)

The two sources will provide data on overall agricultural yield, temperature, precipitation, agricultural investment, pesticide use, land availability, and other relevant features.

## Methodology

The analysis and modeling follow the CRISP-DM technique. The models being used in this study are regressor models, with an expectation to utilize models that support regression type use-cases, such as a multi-linear regression model, random forest regression, and others. Currently, the final model selected is a Random Forest Regressor. Sklearn pipelines and transformers are utilized to make the code and process as repeatable as possible.

Expected Results:

The aim is to deliver a model capable of reliably predicting the agricultural yield of a particular product based on environmental inputs. Given the regression nature of this problem, accuracy will be assessed through MSE/MAE and possibly other metrics as necessary (e.g., R^2).

## Results

Detailed results can be found in the capstone notebook. In addition, all images can be found in the images directory.

Three models were used in this study:

- Linear Regression
- Random Forest Regression
- XGBoost Regression

MAE, MSE, and R^2 showed that the Random Forest Regression model performed the best and therefore was selected as the final model.

Based on the findings from the model, there are several major take-aways:

1. Crop type proves to be the biggest indicator of yield by tonnage and root crops show to produce the most.
2. Pesticide use is the biggest contributor to yield excluding the crop type. Pesticide use tends to have a profound impact on the overall yield. More pesticide use leads to higher crop yield.
3. The year also tends to have an impact on the overall crop yield. This may be due to El Nino/La Nina weather patterns or other historical events like wars, famines, etc.
4. Temperature and Rainfall during critical months shows to influence crop yield. This appears to be roughly during months in the spring and fall which, as we know, are crucial to plant growth.
5. Overall investment in agriculture can influence crop yield but it tends to be less impactful than some of the other features outlined above

The importances can be found in the images directory located [here (all features)](./crop_yield/images/feature_importances.png) and [here (excluding crop types)](./crop_yield/images/feature_importances_no_items.png).

If a region is looking to maximize its agricultural yield, growers need to select more productive crops and consider the use of pesticides to maximize their output. Regions with large temperature fluctuations should be avoided if possible (deserts as an example).

## Next steps

### Expanding Research and Model

This study could be further expanded upon by using more environmental factors or higher fidelity data either in terms of geographical areas (smaller regions) or time (weekly values). Additionally, more models and architectures could be evaluated that could potentially improve the overall accuracy.

### Expanding Access and Deployment

The deployment of the model developed here is limited at best. It's only available within the notebook provided. To provide more access, this could be hosted as a web application with a public URL.

### Driving Further Action to Impact Climate Change

This analysis and report could be shared with political organizations, who in turn, can influence environmental policy and drive action to address climate change. Improving access and deployment as outlined above could facilitate this process.

## Outline of project

- [Link to notebook](capstone.ipynb)

### Contact and Further Information

- Nathan Meek, n.k.meek@gmail.com
