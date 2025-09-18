from langchain_core.tools import tool
import io
import PyPDF2
import requests

starting = 53:27

url="http://arxiv.org/pdf/2509.12181v1"
# Step1: Access PDF via URL
response = requests.get(url)
# print(response.content)
# Step2: Convert to Bytes
pdf_file = io.BytesIO(response.content)
# print(pdf_file)
# Step3: Retrieve Text from PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)
# Extract text from all pages
text = ""
for i, page in enumerate(pdf_reader.pages, 1):
    print(f"Extracting text from page {i}/{num_pages}")
    text += page.extract_text() + "\n"

print(f"Successfully extracted {len(text)} characters of text from PDF")



