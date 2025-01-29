
# PDF to PNG Image Converter

This script converts PDF files into PNG images using the PyMuPDF library. It includes functionalities to exclude certain PDF files based on a list provided in a text file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Usamaniaz219/pdf_2_png_converter_python_code.git
   ```
   
2. Install PyMuPDF:
   ```bash
   pip install pymupdf
   ```

## Usage

### 1. Requirements

- Python 3.x
- PyMuPDF library

### 2. Script Execution

```python
import pymupdf 
import os

def convert_pdfs_2_images(pdf_path, output_folder):
    # Extract the base name of the PDF file without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    pdf_document = pymupdf.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        toc = pdf_document.get_toc()
        print("table of contents:",toc)
        pix = page.get_pixmap()
        
        # Use the PDF name for the output image file, with page number appended
        image_filename = f"{output_folder}/{pdf_name}_page_{page_num + 1}.png"
        pix.save(image_filename)
        print(f"Saved {image_filename}")
    
    pdf_document.close()

# Function to process all PDFs except those listed in the .txt file
def process_txt_file(txt_file_path, pdf_directory, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the .txt file to get the names of the PDFs to exclude
    with open(txt_file_path, 'r') as file:
        exclude_pdfs = {line.strip().replace(".pdf", "") for line in file if line.strip()}

    # List all PDF files in the directory
    for pdf_filename in os.listdir(pdf_directory):
        if pdf_filename.endswith(".pdf"):
            pdf_name = os.path.splitext(pdf_filename)[0]

            # If the PDF is not in the exclusion list, process it
            if pdf_name not in exclude_pdfs:
                pdf_filepath = os.path.join(pdf_directory, pdf_filename)
                print(f"Processing {pdf_filepath}...")

                # Create a subfolder for each PDF's images
                pdf_output_folder = os.path.join(output_folder, pdf_name)
                if not os.path.exists(pdf_output_folder):
                    os.makedirs(pdf_output_folder)

                # Convert the PDF to images
                convert_pdfs_2_images(pdf_filepath, pdf_output_folder)
            else:
                print(f"Skipping {pdf_name}. It is listed in the exclusion file.")

txt_file_path = "/path/to/exclusion_file.txt"
pdf_directory = "/path/to/pdf_files_directory/"
output_folder = "/path/to/output_directory/"

process_txt_file(txt_file_path, pdf_directory, output_folder)
```

### 3. Explanation

- **convert_pdfs_2_images**: Converts each page of a given PDF into a PNG image and saves it in the specified output folder.
- **process_txt_file**: Processes all PDF files in a directory, excluding those listed in the `exclusion_file.txt`. It creates a separate folder for each PDF's images in the output directory.

### 4. Example Usage

- Replace `/path/to/exclusion_file.txt`, `/path/to/pdf_files_directory/`, and `/path/to/output_directory/` with your actual file paths.
- Run the script to convert PDFs to PNG images while excluding specified PDFs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

Feel free to adjust the installation instructions, usage examples, and file paths to suit your project setup.
