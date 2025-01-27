OCR-Numeric-System

Overview

The OCR-Numeric-System is an Optical Character Recognition (OCR) pipeline designed to extract handwritten numeric data (whole numbers and decimal values) from scanned cadastral map images. This system preprocesses input images, detects regions of interest, and applies OCR engines to digitize the handwritten data, ignoring irrelevant text or noise.

Key Features

Numeric Extraction: Extracts whole numbers and decimal values from handwritten content.

Dual OCR Engine: Combines Tesseract OCR and EasyOCR for improved accuracy.

Noise Handling: Handles noisy and low-quality images with preprocessing techniques.

Flexible Output: Saves results in a structured CSV file.

Project Structure

OCR-Numeric-System/
├── input_images/                # Folder containing input cadastral map images
├── output/                      # Folder for outputs (e.g., CSV files)
├── src/                         # Main source code
│   ├── preprocess.py            # Preprocessing scripts
│   ├── inference.py             # OCR engine integration (Tesseract/EasyOCR)
│   ├── postprocess.py           # Post-processing scripts (cleaning/validation)
│   ├── utils.py                 # Utility functions (logging, image handling, etc.)
│   └── main.py                  # Main entry point for running the system
├── requirements.txt             # List of Python dependencies
├── README.md                    # Documentation on how to use the codebase
├── LICENSE                      # License for the project (optional)
└── tests/                       # Unit tests for different components

Installation

Prerequisites

Python 3.7 or higher

pip package manager

GPU (optional, recommended for EasyOCR performance)

Step 1: Clone the Repository
git clone https://github.com/your-repo/OCR-Numeric-System.git
cd OCR-Numeric-System

Step 2: Install Dependencies

Install all required libraries using the requirements.txt file:
pip install -r requirements.txt

Usage

1. Add Input Images

Place scanned cadastral map images (JPG/PNG format) into the input_images/ folder.

2. Run the System

Execute the pipeline by running the main.py script:
python src/main.py

3. View Results

Extracted numeric data will be saved in the output/ folder as a CSV file. The CSV includes columns for:

Image Name

Extracted Numbers

Example Command
python src/main.py

How It Works

Preprocessing

Converts images to grayscale.

Removes noise using Gaussian Blur.

Enhances numeric content visibility with adaptive thresholding.

Cleans small imperfections via morphological operations.

Region Detection

Identifies potential regions of interest (ROIs) using contour detection.

Filters irrelevant regions based on size constraints.

OCR Integration

Tesseract OCR: Extracts numeric content with optimized configuration.

EasyOCR: Handles variations in handwriting and noisy input.

Results from both OCR engines are combined and validated.

Post-Processing

Cleans and validates extracted data using regular expressions.

Filters out irrelevant or invalid text.

Dependencies

opencv-python

pytesseract

easyocr

numpy

csv

For GPU acceleration with EasyOCR:

torch, torchvision, torchaudio
