
import os, subprocess

demo_folder = "../dataset/demo_calls"

for file in os.listdir(demo_folder):
    path = os.path.join(demo_folder, file)
    print("Processing:", path)
    subprocess.run(["python", "extract_demo_data.py", path])
