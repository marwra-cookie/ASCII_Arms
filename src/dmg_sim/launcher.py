import subprocess
import sys
import os
import platform

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
project_root = os.path.dirname(src_dir)


def update():
    """ """
    os.system("cls")


def open_new_window():
    """ """
    system_platform = platform.system()
    module_path = "src.dmg_sim.main"

    if system_platform == "Windows":
        subprocess.Popen(
            [sys.executable, "-m", module_path],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )

    elif system_platform == "Linux":
        subprocess.Popen(
            ["x-terminal-emulator", "-e", f"{sys.executable} -m {module_path}"]
        )

    elif system_platform == "Darwin":  # Darwin = macOS
        subprocess.Popen(
            ["open", "-a", "Terminal", "--args", sys.executable, "-m", module_path]
        )
    else:
        print(f"Unsupported platform: {system_platform}")

    sys.exit()


if __name__ == "__main__":
    open_new_window()
