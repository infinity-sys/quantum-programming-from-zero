# Quantum Programming: From Zero to Hero

The code for the Infinity Systems YouTube course **Quantum Programming: From Zero to Hero**. The course is for computer science and data science students first, and for anyone curious: no physics, and no maths beyond simple arithmetic to start. We write and run real quantum programs with Python and Qiskit, from a first one-qubit circuit to real quantum algorithms.

Playlist: https://www.youtube.com/playlist?list=PLdzFLOpVpeVc

Every episode has a folder in `episodes/` and a git tag (`e01`, `e02`, …), so you can jump to exactly the code you saw in the video. Each program sits next to its real output (`.out` or `.txt`).

## Setup (pick your platform)

You need Python 3.11 or newer (the course uses Python 3.13 and Qiskit 2.6.1).

| Platform | Install Python |
|---|---|
| macOS | `brew install python@3.13` |
| Windows | python.org installer (tick "Add python.exe to PATH"), or `winget install Python.Python.3.13` |
| Linux: Ubuntu / Debian | `sudo apt install python3 python3-venv python3-pip` |
| Linux: Fedora | `sudo dnf install python3 python3-pip` |
| Linux: Arch | `sudo pacman -S python python-pip` |
| No install | Google Colab: `!pip install qiskit qiskit-aer` in the first cell |

Then, in the repository folder:

```
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python episodes/E01/first_circuit.py
```

You should see the circuit drawing and counts close to `{'0': 500, '1': 500}`.

## Episodes

| Episode | Topic | Code |
|---|---|---|
| E01 | What is quantum computing? Your first quantum program | `episodes/E01` |
| E02 | Setting up: Python, Qiskit and your first notebook | `episodes/E02` |
| E03 | The Python you need for quantum computing | `episodes/E03` |
| E04 | Bits, binary and logic gates | `episodes/E04` |

## License
MIT, see LICENSE.
