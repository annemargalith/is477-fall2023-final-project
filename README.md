# UCI Iris Dataset

## Overview: 

This repository has the purpose of applyign the reproducibility concept when performing different analysis in the UCI Iris Dataset. Reproducibility is an important concept in which we use the same inputs and methods to try to get the same results. By applying it in this repository, we will be looking at the transparency of the study, the different license types and copyrights from the data and software, as well as how to properly cite the data and how to identify issues when trying to reproduce results. 


## Data Availability

**UCI Iris Dataset**
- The dataset was taken from the UC Irvine Machine Learning Repository (DOI: 10.24432/C56C76)

- The UCI Machine Learning Repository containing the dataset is under the following citation: 
Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.

- License: This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. It allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

- Therefore, under this license, we will be including the dataset in our repository, since, with the right credit given, it can be shared. The data is contained in the iris folder inside our data folder of this repository.

## Analysis

The summary statistics for the Iris dataset are as follows:

Sepal Length: Ranges from 4.3 to 7.9 cm, with an average of 5.84 cm.
Sepal Width: Ranges from 2.0 to 4.4 cm, with an average of 3.05 cm.
Petal Length: Ranges from 1.0 to 6.9 cm, with an average of 3.76 cm.
Petal Width: Ranges from 0.1 to 2.5 cm, with an average of 1.20 cm

Key Insights from the Iris Dataset Pair Plot:
Distinct Species Characteristics:
Iris Setosa often stands out as distinctly different in the scatter plots, especially in relation to petal length and petal width. It typically has smaller petal lengths and widths compared to the other two species.
Iris Versicolor and Iris Virginica show more overlap in their features but can still be distinguished, especially when looking at the combination of petal length and petal width.
Feature Relationships:
There is a strong positive correlation between petal length and petal width for all species. This indicates that as petal length increases, petal width tends to increase as well.
Sepal length and sepal width show a more complex relationship, with less clear correlation patterns. This suggests these features might not be as effective for species differentiation compared to petal measurements.
Feature Distributions:
The distribution of petal lengths and widths shows a more distinct separation between species compared to sepal lengths and widths. For example, Iris Setosa might have a distinctly narrow range of small petal lengths and widths, while Versicolor and Virginica have larger ranges.
Sepal width and length distributions might show more overlap between the species, indicating these features are less discriminative.
Species Overlap:
Iris Versicolor and Virginica tend to overlap in several feature combinations, but some separation can still be observed, especially in petal dimensions.
Iris Setosa is generally well-separated in all feature combinations, making it the most distinct of the three species in terms of these measured features.
Outliers and Variations:
There might be a few outliers, especially in the plots involving sepal width and length. These could be due to natural variations or measurement errors.
The variance within Iris Setosa for most features is generally lower compared to the other two species, indicating more uniformity in its feature measurements.
Conclusion:
The pair plot suggests that petal measurements (length and width) are more effective for differentiating between the three species of Iris compared to sepal measurements.
Iris Setosa can be easily distinguished from the other two species, while Versicolor and Virginica are more challenging to differentiate based solely on these four features.
These insights can be particularly valuable in designing classification models or conducting further species-specific analyses.
This analysis is based on typical observations from the Iris dataset. The exact patterns and insights could vary depending on the specific dataset instance and plot detail

## Workflow


## Reproducing

## License

## References