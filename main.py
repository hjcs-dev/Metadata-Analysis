import exifread
from PyPDF2 import PdfFileReader
import os

def extract_image_metadata(file_path):
    print(f"Metadata for image: {file_path}")
    try:
        with open(file_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
            for tag in tags.keys():
                print(f"{tag}: {tags[tag]}")
    except Exception as e:
        print(f"Error reading image metadata: {e}")

def extract_pdf_metadata(file_path):
    print(f"Metadata for PDF: {file_path}")
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            info = pdf_reader.getDocumentInfo()
            for key, value in info.items():
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error reading PDF metadata: {e}")

def main():
    file_path = input("Enter the path to the file: ").strip()
    
    if not os.path.isfile(file_path):
        print("The provided path does not exist or is not a file.")
        return

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
        extract_image_metadata(file_path)
    elif file_path.lower().endswith('.pdf'):
        extract_pdf_metadata(file_path)
    else:
        print("Unsupported file type. Please provide a JPG, JPEG, PNG, TIFF, BMP, or PDF file.")

if __name__ == "__main__":
    main()
