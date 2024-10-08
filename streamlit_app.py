import streamlit as st
import PyPDF2
from ai_document import generate_ai_response

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text_from_txt(file):
    return file.read().decode('utf-8')

# Streamlit UI
st.title("📄 AI Document")
st.subheader("AI Document adalah aplikasi inovatif yang memanfaatkan kecerdasan buatan untuk membantu pengguna dalam memahami dan menganalisis dokumen dengan lebih efisien.")

uploaded_file = st.file_uploader("Unggah file ", type=("pdf", "txt", "docx"))

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        document_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document_text = extract_text_from_docx(uploaded_file)
    elif uploaded_file.type == "text/plain":
        document_text = extract_text_from_txt(uploaded_file)
    else:
        st.error("Format file tidak didukung.")
        document_text = ""

    if document_text:
        
        user_input = st.text_area("Masukkan pertanyaan Anda tentang dokumen:")
        
        if st.button("Dapatkan Respon"):
            if user_input:
                full_input = f"{user_input}\n\nDokumen:\n{document_text}"
                response = generate_ai_response(full_input)
                st.subheader("Respon AI:")
                st.write(response.candidates[0].content.parts[0].text)
            else:
                st.error("Silakan masukkan pertanyaan atau permintaan Anda.")

