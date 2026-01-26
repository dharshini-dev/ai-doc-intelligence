AI Document Intelligence System (Self-Hosted)
Project Overview
This is a self-hosted AI system designed to extract structured data from identity documents. It uses a local OCR engine to read text and a Large Language Model (Llama 3) to format the data into JSON.

Tech Stack
UI: Streamlit

OCR: EasyOCR

LLM: Llama 3 (via Ollama)

Hosting: 100% Local / Self-hosted

Key Features
Data Privacy: Works offline; sensitive documents never leave the local system.

Accuracy: Uses Llama 3 (4.7 GB) for high-precision extraction.

JSON Output: Automatically generates machine-readable JSON data.

How to Run
Install Requirements: pip install -r requirements.txt

Start LLM Server: Open terminal and run: ollama run llama3

Run Application: streamlit run app.py

Implementation Steps
Text Extraction: Image text is captured using EasyOCR.

AI Processing: Raw text is sent to the local Ollama API.

Data Structuring: The LLM processes the text and returns specific fields like Name, DOB, and License Number in JSON format.