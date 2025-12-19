# Static Site Generator (SSG)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Build](https://img.shields.io/badge/Build-SSG-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

A lightweight, modular **Static Site Generator** written in Python. This tool uses a component-based architecture to define layouts (Boxes and Cells) and renders them into static assets using a custom graphics engine.

---

## 🏗️ Architecture & Modules

The project is structured to separate site logic from the rendering engine:

* **`main.py`**: The orchestrator. Manages the generation process and site assembly.
* **`graphics.py`**: The core rendering engine that handles layout placement and visual output.
* **`cell.py` & `box.py`**: Atomic design components used to define grid systems and content containers.
* **`popup.py`**: Logic for generating interactive or overlay elements within the static output.
* **`images/`**: Directory for source assets and rendered visual components.

---

## 🚀 Key Features

- **Component-Based Design:** Define your site using reusable `Cell` and `Box` objects.
- **Custom Graphics Engine:** Bypasses heavy frameworks for a lightweight, code-first generation approach.
- **Automated Workflow:** Build and export static structures with a single command.
- **Modular UI:** Includes dedicated logic for popups and navigation elements.

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Requirements listed in `requirements.txt`

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/azhagan2/ssg-project-name.git](https://github.com/azhagan2/ssg-project-name.git)
   cd ssg-project-name

2. ** Install Dependencies ** 
 
   ```pip install -r requirements.txt```

3. ** Run the project **

   ```python main.py```

---

📄 License

Distributed under the MIT License. See LICENSE for more information.

---

<p align="center"> Built with ❤️ by <a href="https://www.google.com/search?q=https://github.com/azhagan2">azhagan2</a> </p>
