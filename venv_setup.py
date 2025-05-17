import os
import subprocess
import sys

def setup_venv():
    if not os.path.exists("venv"):
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("✅ Virtual environment created.")
    else:
        print("✅ Virtual environment already exists.")

    pip_exec = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "pip")
    subprocess.run([pip_exec, "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed in virtual environment.")

if __name__ == "__main__":
    setup_venv()
