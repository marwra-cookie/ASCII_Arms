import subprocess
import sys
import os
import platform

columns = 80
rows = 20


def update():
    os.system("cls")


def open_new_window(path):
    system_platform = platform.system()

    if system_platform == "Windows":
        subprocess.Popen(
            [sys.executable, path], creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    elif system_platform == "Linux":
        subprocess.Popen(["x-terminal-emulator", "-e", f"{sys.executable} {path}"])

    elif system_platform == "Darwin":  # Darwin = macOS
        subprocess.Popen(["open", "-a", "Terminal", path])
    else:
        print(f"Unsupported platform: {system_platform}")

    sys.exit()


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(current_dir, "main.py")

    if not os.path.exists(main_path):
        print(f"Error: main.py not found at {main_path}")
    else:
        open_new_window(main_path)
