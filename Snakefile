rule prepare:
  shell:
    "python scripts/prepare_data.py"

rule profile:
  shell:
    "python scripts/profiles.py"

rule analyze:
  shell:
    "python scripts/analysis.py"