import re

def clean_and_validate_numbers(text):
    valid_numbers = re.findall(r'\b\d+\.\d+\b|\b\d+\b', text)
    return valid_numbers

def save_to_csv(results, output_csv):
    import csv
    import os
    import time

    if os.path.exists(output_csv):
        output_csv = "output_" + str(int(time.time())) + ".csv"

    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Image Name", "Extracted Numbers"])
        for image_name, numbers in results:
            writer.writerow([image_name, ", ".join(numbers)])
    print(f"Results saved to {output_csv}.")
