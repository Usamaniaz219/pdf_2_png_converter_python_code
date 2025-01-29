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

txt_file_path = "/home/usama/Git _text_file"
pdf_directory = "/media/usama/SSD/Usama_dev_ssd/map_links_23_sep/renamed_pdf_testing/"
output_folder = "/media/usama/SSD/Usama_dev_ssd/Png_images_17_oct_2024/"

process_txt_file(txt_file_path, pdf_directory, output_folder)





































































































