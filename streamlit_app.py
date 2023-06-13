import streamlit as st
from PIL import Image
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe' 
def textfromimage(image):
    with Image.open(image) as img:
        img = img.convert('L')
        extracted_text = pytesseract.image_to_string(img)
    return extracted_text

def main():
    st.title("Text Extraction")
    upload_image = st.file_uploader("Upload an image file", type=['png','jpg','jpeg'])
    if upload_image is not None:
        st.image(upload_image, caption = 'uploaded image', use_column_width = True)
        extracted_text = textfromimage(upload_image)
        st.header("Extracted Data")
        st.text(extracted_text)
        

    extraction_time = st.time_input("Select the extraction time")
    scheduled_time = datetime.datetime.combine(datetime.date.today(),extraction_time)
    st.header("Scheduled Time")
    st.text(scheduled_time)
    # if scheduled_time == datetime.datetime.now():
       

if __name__ == '__main__':
    main()