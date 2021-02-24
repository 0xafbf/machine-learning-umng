

import subprocess

# runs <base_name>.py and writes it to <base_name>.md
def run(base_name):
    file_path = base_name + ".py"
    print("building", file_path)
    output = subprocess.run(["python", file_path], capture_output=True, text=True).stdout
    output_path = base_name + ".md"
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(output)

parts = ["metadata.yaml"]
parts.append("00_theory.md")

run("01_linear")
parts.append("01_linear.md")

run("02_multi")
parts.append("02_multi.md")

run("03_logistic")
parts.append("03_logistic.md")

parts.append("04_conclusion.md")

def build(output_file):

    command = [
        "pandoc",
        "--standalone",
        "--output", output_file,
    ]

    command += parts
    subprocess.run(command)

build("single.html")
# build("single.pdf")
