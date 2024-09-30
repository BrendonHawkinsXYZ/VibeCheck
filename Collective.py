import subprocess
import time
import sys

# Define the script names
scripts = ["OnDevices.py", "Segmented.py", "Gradient.py"]

# Define the delay in seconds
delay = 3

# Get the current Python interpreter path
python_executable = sys.executable

# Run each script with the specified delay
for script in scripts:
    try:
        print(f"Running {script}...")
        subprocess.run([python_executable, script])
        print(f"{script} finished. Waiting for {delay} seconds before next script...")
        time.sleep(delay)
    except Exception as e:
        print(f"An error occurred while running {script}: {e}")

print("All scripts have been executed.")
