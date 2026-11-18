import streamlit as st
from google import genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def get_gemini_response(prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set. Add it to a .env file.")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage matching based
on the job description and list the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if not jd.strip():
        st.warning("Please paste the job description.")
    elif uploaded_file is None:
        st.warning("Please upload a resume PDF.")
    else:
        try:
            text = input_pdf_text(uploaded_file)
            if not text.strip():
                st.error("Could not extract text from the PDF. Please upload a text-based PDF.")
            else:
                prompt = input_prompt.format(text=text, jd=jd)
                response = get_gemini_response(prompt)
                st.subheader(response)
        except Exception as exc:
            st.error(f"Unable to generate the ATS evaluation: {exc}")