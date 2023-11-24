from ucimlrepo import fetch_ucirepo 
  
# fetch dataset to find out variables used
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
print(iris.variables) 

import pandas as pd

# formatting dataset and making columns according to variables found
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv('./data/iris/iris.data', header=None, names=column_names)

# displaying head
print(iris_data.head())

# finding summary statistics
summary_statistics = iris_data.describe()
print(summary_statistics)

# making pair plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(iris_data, hue="class")

# Show the plot
plt.show()