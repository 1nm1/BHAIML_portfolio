### Agricultural Yield Prediction From Environmental Factors

**Nathan Meek**

#### Executive summary

#### Rationale

As the world continues to warm through climate change, food available and security is increasingly at risk. Understanding the expected yields for certain products in various regions of the world can give insight into where food scarcity might become a pressing issue in the future. This understanding is critical for planning and implementing strategies to mitigate the impact of climate change on agriculture.

Predictive models can be developed to forecast crop yields under different climate scenarios, allowing policymakers and farmers to make informed decisions about crop selection, irrigation practices, and resource allocation. International cooperation and investment in sustainable agricultural technologies will be essential to enhance food security globally, especially in areas most susceptible to the adverse effects of climate change.

#### Research Question

Can we model agricultural yield based on environmental factors especially as become more unpredictable due to climate change?

#### Data Sources

- [Food and Agriculture Organization of the United Nations (FAOSTAT)](https://www.fao.org/faostat/en/#data)

- [World Bank Group Climate Change Portal](https://climateknowledgeportal.worldbank.org)

The two sources will provide data on overall agricultural yield, temperature, precipitation, pesticide use, land availability, and other relevant features.

#### Methodology

The analysis and modeling follow the CRISP-DM technique. The models being used in this study are regressor models, with an expectation to utilize models that support regression type use-cases, such as a multi-linear regression model, random forest regression, and others. Currently, the final model selected is a Random Forest Regressor. Sklearn pipelines and transformers are utilized to make the code and process as repeatable as possible.

Expected Results:

The aim is to deliver a model capable of reliably predicting the agricultural yield of a particular product based on environmental inputs. Given the regression nature of this problem, accuracy will be assessed through MSE/MAE and possibly other metrics as necessary (e.g., R^2).

#### Results

Based on the findings from the model, there are three major take-aways:

1. What you're growing can have a profound impact on the overall yield. Root crops tend to produce much more than other crops.
2. Pesticide use is the biggest contributor to yield if the type of crop is ignored. Pesticide use tends to have a profound impact on the overall yield.
3. Temperature appears to have more of an influence versus rainfall. This could be an important finding as heat waves or domes may lead to more crop loss vs drought (although both are damaging).

The importances can be found in the images directory located [here (all features)](./crop_yield/images/feature_importances.png) and [here (no crop types in features)](./crop_yield/images/feature_importances_no_items.png)

If a region is looking to maximize its agricultural yield, growers need to select more productive crops and consider the use of pesticides to maximize their output. Regions with large temperature fluctuations should be avoided if possible (deserts as an example).

#### Next steps

What suggestions do you have for next steps?

#### Outline of project

- [Link to notebook 1]()

##### Contact and Further Information

- Nathan Meek, n.k.meek@gmail.com
