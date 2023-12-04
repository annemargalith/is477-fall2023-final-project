import pandas as pd
from ydata_profiling import ProfileReport

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv('./data/iris/iris.data', header=None, names=column_names)

from ydata_profiling import ProfileReport

# Generate the profiling report
profile = ProfileReport(df, title='Profiling Report')

# Write the report to an HTML file
profile.to_file("profiling/report.html")