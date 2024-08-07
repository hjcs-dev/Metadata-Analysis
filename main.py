import exifread
import PyPDF2
import os

def extract_image_metadata(image_path):
    """Extracts and prints EXIF metadata from an image file."""
    try:
        print(f"Opening image file: {image_path}")
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            if not tags:
                print("No metadata found.")
            else:
                print(f"Metadata for image: {image_path}")
                for tag in tags.keys():
                    print(f"{tag}: {tags[tag]}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_pdf_metadata(pdf_path):
    """Extracts and prints metadata from a PDF file."""
    try:
        print(f"Opening PDF file: {pdf_path}")
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            info = reader.getDocumentInfo()
            if not info:
                print("No metadata found.")
            else:
                print(f"Metadata for PDF: {pdf_path}")
                for key, value in info.items():
                    print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt user for file path
    file_path = input("Enter the path to the file: ").strip()
    
    # Validate file path
    if not os.path.isfile(file_path):
        print("The file does not exist or is not a valid file path.")
        return

    # Determine file type and extract metadata
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
        extract_image_metadata(file_path)
    elif file_path.lower().endswith('.pdf'):
        extract_pdf_metadata(file_path)
    else:
        print("Unsupported file type. Please provide an image or PDF file.")

if __name__ == "__main__":
    main()
