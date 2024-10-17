import os
import shutil

def move_map_directories(source_dir, destination_dir):
    # Check if the destination directory exists; if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate over items in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        # Check if the item is a directory and ends with "_maps"
        if os.path.isdir(item_path) and item.endswith("_maps"):
            # Move the directory to the destination
            shutil.move(item_path, destination_dir)
            print(f"Moved: {item_path} -> {destination_dir}")

# Example usage
source_directory = "/home/usama/Home_data/Png_format_image_extractor_from_the_pdf_file_7_oct_2024/output_png_images_from_pdf_33/"
destination_directory = "/home/usama/Home_data/Png_format_image_extractor_from_the_pdf_file_7_oct_2024/Cites_containing_only_map_images_8_oct_2024/"

move_map_directories(source_directory, destination_directory)
