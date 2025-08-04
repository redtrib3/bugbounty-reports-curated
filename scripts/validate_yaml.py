'''
Validate the yaml files
'''
import os
import yaml

error_log = {}

report_path = "reports/"
for filename in os.listdir(report_path):
    if filename.endswith(".yaml") or filename.endswith(".yml"):
        try:
            with open(report_path + filename, "r", encoding="utf-8") as f:
                yaml.safe_load(f)
        except yaml.YAMLError as e:
            error_log[filename] = str(e).splitlines()[0]  # just the first line of the error

if error_log:
    print("Files with YAML errors:\n")
    for file, err in error_log.items():
        print(f"{file}: {err}")
else:
    print("All YAML files parsed successfully.")
