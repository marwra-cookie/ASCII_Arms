# DMG-SIM
**DMG-SIM** is a modular CLI based damage simulation system, built with Python. 
It simulates interactions between game entities, items, and spells using customizable data from JSON configuration files. 
This tool is useful for prototyping game mechanics, balancing combat systems, or serving as a backend module in larger game engines.

---

## 🛠 Requirements
- Python 3.13 or higher
- Git (optional, if cloning the repo)

## 💻 Installation

1. **Clone repository**
   ```bash
   git clone <repository-url>
   ```
   ```bash
   cd DMG-SIM
   ```
2. **Create virtual environment (recommended)**
   ```bash
    python -m venv .venv
   ```
   **Windows**
   
   &nbsp; PowerShell
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   &nbsp; Command Prompt
   ```bash
   .\.venv\Scripts\Activate.bat
   ```
   **Mac OS / Linux**
   ```bash
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   &nbsp;pip install .
   ```
4. **Run game**
   ```bash
   python -m src.dmg_sim.main
   ```