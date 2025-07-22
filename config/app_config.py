import streamlit as st

class AppConfig:
    """Application configuration and constants for PDFSense
    Customized by Arideep Kanshabanik
    """

    APP_TITLE = "PDFSense"
    APP_ICON = "📘"
    LAYOUT = "wide"

    # Supported operations
    OPERATIONS = {
        "home": "🏠 Home",
        "convert": "🔁 Convert PDF", 
        "split": "✂️ Split PDF",
        "merge": "➕ Merge PDFs",
        "compress": "🗜️ Compress PDF"
    }

    # File type configurations
    SUPPORTED_FORMATS = {
        "pdf": ["pdf"],
        "images": ["png", "jpg", "jpeg"],
        "documents": ["docx", "txt"]
    }

    # Compression settings
    COMPRESSION_LEVELS = {
        "Low": {"quality": 85, "dpi": 150},
        "Medium": {"quality": 70, "dpi": 120}, 
        "High": {"quality": 50, "dpi": 96}
    }

    @classmethod
    def setup_page(cls):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title=cls.APP_TITLE,
            page_icon=cls.APP_ICON,
            layout=cls.LAYOUT
        )
