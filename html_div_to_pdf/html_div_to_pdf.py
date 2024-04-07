import os
from bs4 import BeautifulSoup
import pdfkit

documents_dir = os.path.expanduser("~/Documents")

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_div(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # div_element = soup.find('div', class_=div_class)
    return str(soup)

def generate_pdf(html_content, output_filename):
    output_path = os.path.join(documents_dir, output_filename)
    try:
        pdfkit.from_string(html_content, output_path)
        print("PDF generated successfully!")
    except Exception as e:
        print("Error generating PDF:", e)

html_file_path = '/home/eddy-di/Downloads/result.aqualab.kg.html'
# div_id = 'page'
output_filename = "output.pdf"

html_content = read_html_file(html_file_path)
# specific_div = extract_div(html_content, div_id)
full_page_content = extract_div(html_content)
print("Extracted page content:", full_page_content)
generate_pdf(full_page_content, output_filename)
