from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the tessdata directory to the folder containing your traineddata file
pytesseract.pytesseract.tessdata_dir_config = r'--tessdata-dir "E:\arabic"'

# Read an image
image = Image.open(r'C:\Users\pc\Documents\Bandicam\output_text\text1.JPG')

# Use PyTesseract to extract text with Arabic language
text = pytesseract.image_to_string(image, lang='ara')

# Specify the output file path
output_file_path = r'C:\Users\pc\Documents\Bandicam\output_text\file.txt'

# Save the extracted text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text)
print("done")

