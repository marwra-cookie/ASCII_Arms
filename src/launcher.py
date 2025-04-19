import subprocess
import os

columns = 80
rows = 20

if __name__ == "__main__":
    script_path = os.path.abspath("src\\main.py")
    print(script_path)
    subprocess.Popen(
        f'start cmd /k "mode con: cols={columns} lines={rows} && python "{script_path}""',
        shell=True,
    )
