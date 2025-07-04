
import subprocess
import sys

def install_packages():
    packages = [
        "opencv-python",
        "numpy"
    ]
    for package in packages:
        print(f"Instalando {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_packages()
