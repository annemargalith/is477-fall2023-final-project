rule prepare:
  output:
    "data/iris"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input: 
    "data/iris"
  output:
    'profiling/report.html'
  shell:
    "python scripts/profiles.py"

rule analyze:
  input:
    "data/iris"
  output:
    'results'
  shell:
    "python scripts/analysis.py"