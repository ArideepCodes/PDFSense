import streamlit as st
from PIL import Image

class UILayout:
    """✨ Handles all UI layout and rendering for PDFSense ✨

    © Created by Arideep Kanshabanik
    """

    def __init__(self):
        pass

    def render_header(self):
        st.markdown(
            """
            <div style='text-align: center; margin-bottom: 30px;'>
                <h1 style='color: #4CAF50;'>📘 PDFSense</h1>
                <h4 style='color: #555;'>All-in-One PDF Management Toolkit</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    def render_sidebar(self):
        st.sidebar.image("assets/pdf_logo.png", width=180)
        st.sidebar.title("📂 PDFSense Menu")
        option = st.sidebar.radio(
            "Select an operation",
            (
                "🏠 Home",
                "🔁 Convert PDF",
                "✂️ Split PDF",
                "➕ Merge PDFs",
                "🗜️ Compress PDF",
            )
        )

        # 👉 Contact Us section
        st.sidebar.markdown("---")
        st.sidebar.markdown("📧 **Contact Us**")
        st.sidebar.markdown("[arideepkanshabanik@gmail.com](mailto:arideepkanshabanik@gmail.com)")

        return option

    def render_home_page(self):
        st.markdown("## 👋 Welcome to PDFSense!")
        st.markdown(
            """
            PDFSense is your all-in-one solution for managing PDF documents effortlessly.

            **Key Features:**
            - 🔁 Convert PDFs to Word, Text, or Images
            - ✂️ Split large PDFs by page range
            - ➕ Merge multiple PDFs into one
            - 🗜️ Compress PDFs while retaining quality

            ---
            """
        )
        st.success("Select an operation from the sidebar to get started.")

    # ✅ Updated to support 'multiple' uploads and 'help_text'
    def render_file_uploader(self, label, file_types, multiple=False, help_text=None):
        return st.file_uploader(
            label,
            type=file_types,
            accept_multiple_files=multiple,
            help=help_text
        )

    def render_download_button(self, label, data, file_name, mime):
        return st.download_button(label, data, file_name=file_name, mime=mime)

    def render_info(self, message):
        st.info(message)

    def render_warning(self, message):
        st.warning(message)

    def render_error(self, message):
        st.error(message)

    def render_success(self, message):
        st.success(message)
