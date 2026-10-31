# E02: Setting Up: Python, Qiskit and Your First Notebook

Video: https://youtu.be/7EHZTxlaMfU

## This episode
1. Install Python (see the table in the main README) and check it: `python3 --version`.
2. Make a project folder and a virtual environment: `python3 -m venv .venv`, then activate it.
3. `pip install -r requirements.txt` (Qiskit 2.6.1, Qiskit Aer 0.18.2, JupyterLab, matplotlib).
4. Run the script: `python episodes/E02/first_circuit.py`. Three real runs: `run1.txt`, `run2.txt`, `run3.txt`.
5. Start JupyterLab (`jupyter lab`) and open `my_first_circuit.ipynb`: the same circuit, cell by cell, with a histogram.

No install? Use Google Colab, and run `!pip install qiskit qiskit-aer` in the first cell.
