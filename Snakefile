rule prepare:
  output:
    "data/iris"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "scripts/prepare_data.py"
  output:
    'profiling/report.html'
  shell:
    "python scripts/profiles.py"

rule analyze:
  input:
    "scripts/prepare_data.py"
  output:
    'results'
  shell:
    "python scripts/analysis.py"