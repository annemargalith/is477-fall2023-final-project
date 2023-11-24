from ucimlrepo import fetch_ucirepo 
  
# fetch dataset to find out variables used
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

with open('./results/iris_variables.txt', 'w') as f:
   f.write(str(iris.variables))

import pandas as pd

# formatting dataset and making columns according to variables found
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv('./data/iris/iris.data', header=None, names=column_names)

# finding summary statistics
summary_statistics = iris_data.describe()
with open('./results/iris_summary_stats.txt', 'w') as f:
   f.write(str(summary_statistics))

# making pair plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(iris_data, hue="class")

plt.savefig('./results/pair_plot.png')
# Show the plot
plt.show()