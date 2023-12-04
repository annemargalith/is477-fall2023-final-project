rule prepare:
  output:
    "data/iris"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  output:
    'profiling/report.html'
  shell:
    "python scripts/profiles.py"

rule analyze:
  output:
    'results'
  shell:
    "python scripts/analysis.py"