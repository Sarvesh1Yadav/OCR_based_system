import pytesseract
import easyocr
from preprocess import preprocess_image
import cv2

def extract_text_regions(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if 10 < w < 300 and 10 < h < 100:  # Filter out small contours
            regions.append((x, y, w, h))
    return regions

# OCR with Tesseract, optimized for decimals and numeric values
def ocr_with_tesseract(region):
    config = "--psm 8 -c tessedit_char_whitelist=0123456789."
    text = pytesseract.image_to_string(region, config=config)
    return text.strip()

# OCR with EasyOCR for better handling of handwritten and noisy text
def ocr_with_easyocr(region):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(region)
    extracted_text = []
    for detection in result:
        text = detection[1]
        extracted_text.append(text)
    return extracted_text

def process_image(image_path):
    preprocessed = preprocess_image(image_path)
    regions = extract_text_regions(preprocessed)
    numeric_data = []

    for x, y, w, h in regions:
        cropped = preprocessed[y:y + h, x:x + w]

        text_tesseract = ocr_with_tesseract(cropped)
        text_easyocr = ocr_with_easyocr(cropped)

        all_text = text_tesseract + " " + " ".join(text_easyocr)
        numeric_data.extend(clean_and_validate_numbers(all_text))

    return numeric_data
