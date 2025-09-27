# Step1: Install tectonic & Import deps
from os import path
import shutil
from typing import final
from langchain_core.tools import tool
from datetime import date, datetime
from pathlib import Path
import subprocess
import shutil




@tool
def render_latex_pdf(latex_content: str) -> str:
    """Render a LaTeX document to PDF.

    Args:
        latex_content: The LateX document content as a string

    Return:
        Path to the generate PDF document
    """

    if shutil.which("tectonic") is None:
        raise RuntimeError(
            "tectonic is not installed. install it first on your system."
        )

    try:
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

        result = subprocess.run(
            ["tectonic", tex_filename, "--outdir", str(output_dir)],
            cwd=output_dir,
            capture_output=True,
            text=True,
            )


        final_pdf = output_dir / pdf_filename
        if not final_pdf.exists():
            raise FileNotFoundError("PDF file was not generated")
        
        print(f"Successfully generated PDF at {final_pdf}")
        return str(final_pdf)
    except Exception as e:
        print(f"Error rendering Latex: {str(e)}")
        raise











