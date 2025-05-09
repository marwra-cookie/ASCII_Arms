# DMG-SIM
**DMG-SIM** is a modular CLI based damage simulation system, built with Python. 
It simulates interactions between game entities, items, and spells using customizable data from JSON configuration files. 
This tool is useful for prototyping game mechanics, balancing combat systems, or serving as a backend module in larger game engines.

---

## 🛠 Installation [WIP]

### 📦 Prerequisites
- Python 3.13 or higher
- Git (optional, if cloning the repo)

### 💻 Windows, Mac OS, or Linux

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DMG-SIM
2. **Create a virtual environment (recommended)**
   ```bash
    python -m venv .venv
    source .venv/bin/activate    # macOS/Linux
    .venv\Scripts\activate       # Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the game simulation**
   ```bash
   python src/dmg_sim/launcher.py