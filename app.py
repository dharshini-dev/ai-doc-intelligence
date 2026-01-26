import streamlit as st
import easyocr
import requests
import numpy as np
from PIL import Image
import json

# 1. Setup Page & Title
st.set_page_config(page_title="AI Doc Intern Task")
st.title("🤖 AI Document Intelligence System")
st.markdown("**Intern Task:** Driving License Extractor (MVP)")

# 2. Initialize OCR Engine
@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en']) 

reader = load_ocr()

# 3. AI Processing Function (Ollama)
def extract_with_ollama(raw_text):
    url = "http://localhost:11434/api/generate"
    
    prompt = f"""
    You are a data extraction assistant.
    Extract the following fields from the raw text provided below.
    Return the output strictly as a JSON object. Do not add any conversational text.
    
    Required JSON Fields:
    - document_type (Set this to "Driving License")
    - name
    - dob
    - license_number
    - issue_date
    - expiry_date
    - address

    Raw Text:
    {raw_text}
    """
    
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    
    try:
        response = requests.post(url, json=payload)
        response_json = response.json()
        return json.loads(response_json['response'])
    except Exception as e:
        return {"error": f"Failed to connect to Ollama. Is it running? Error: {str(e)}"}

# 4. Frontend UI Flow
st.subheader("1️⃣ Upload Document")
uploaded_file = st.file_uploader("Upload Driving License (Image)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Document", use_column_width=True)
    
    if st.button("Extract Information"):
        with st.spinner("Processing Step 1: OCR Text Extraction..."):
            image_np = np.array(image)
            result = reader.readtext(image_np, detail=0)
            extracted_text = " ".join(result)
            
            with st.expander("See Raw OCR Text"):
                st.text(extracted_text)

        with st.spinner("Processing Step 2: AI Analysis (Ollama)..."):
            structured_data = extract_with_ollama(extracted_text)
            st.subheader("2️⃣ Extracted Insights (JSON)")
            st.json(structured_data)