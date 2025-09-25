# Step1: Install tectonic & Import deps
from os import path
import shutil
from langchain_core.tools import tool
from datetime import date, datetime
from pathlib import Path
import subprocess
import shutil


sample_latex_data = r"""
\documentclass{article}
\begin{document}
Hello, world! from LaTex to PDF with Python.
\end(document)
"""

# Step2:  Create directory
output_dir = Path("output").absolute()
output_dir.mkdir(exist_ok=True)

# Step3:  Setup filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
tex_filename = f"paper_{timestamp}.tex"
pdf_filename = f"paper_{timestamp}.pdf"

# Step:  Export as tex & pdf
tex_file = output_dir / tex_filename
tex_file.write_text(sample_latex_data)