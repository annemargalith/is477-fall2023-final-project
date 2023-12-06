rule prepare:
  output:
    "data/iris/iris.data"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input: 
    "data/iris/iris.data"
  output:
    'profiling/report.html'
  shell:
    "python scripts/profiles.py"

rule analyze:
  input:
    "data/iris/iris.data"
  output:
    'results/pair_plot.png'
  shell:
    "python scripts/analysis.py"

rule reproduce: 
  input: 
    'results/pair_plot.png',
    'profiling/report.html'