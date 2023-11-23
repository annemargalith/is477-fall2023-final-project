import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/iris/iris.data')

from ydata_profiling import ProfileReport

# Generate the profiling report
profile = ProfileReport(df, title='Profiling Report')

# Write the report to an HTML file
profile.to_file("profiling/report.html")