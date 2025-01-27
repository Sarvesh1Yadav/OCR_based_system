import os
from inference import process_image
from postprocess import save_to_csv

def process_images(input_folder, output_csv):
    results = []
    for image_name in os.listdir(input_folder):
        if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, image_name)
            numbers = process_image(image_path)
            results.append((image_name, numbers))
            print(f"Processed {image_name}: {numbers}")
    save_to_csv(results, output_csv)

if __name__ == "__main__":
    input_folder = "input_images"  # Folder where scanned images are stored
    output_csv = "output.csv"  # Output CSV file to store the results
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please create it and add images.")
    else:
        process_images(input_folder, output_csv)
