import streamlit as st
from imagem_para_pdf import imagem_para_pdf
import tempfile

st.set_page_config(page_title="OCR para PDF", layout="centered")
st.title("OCR: Imagem para PDF Editável")

st.markdown("""Envie uma imagem (JPG/PNG), escolha o idioma, e baixe o PDF com o texto extraído.""")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["png","jpg","jpeg"])
idioma = st.selectbox("Idioma do OCR", ["por", "eng", "spa"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
        tmp_img.write(uploaded_file.read())
        tmp_img_path = tmp_img.name

    pdf_path = tmp_img_path.replace(".png", ".pdf")
    imagem_para_pdf(tmp_img_path, pdf_path, idioma=idioma)

    st.success("PDF gerado com sucesso!")
    with open(pdf_path, "rb") as f:
        st.download_button("Baixar PDF", f.read(), file_name="saida.pdf")