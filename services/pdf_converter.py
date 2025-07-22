import streamlit as st
from pdf2docx import Converter
from services.base_service import BaseService

class PDFConverterService(BaseService):
    """Service for PDF conversion operations"""

    def convert(self, uploaded_file, conversion_type):
        """Convert PDF based on conversion type"""
        conversion_map = {
            "PDF to Word (.docx)": self._convert_to_word
        }

        converter = conversion_map.get(conversion_type)
        if converter:
            return converter(uploaded_file)
        else:
            raise ValueError(f"Unknown conversion type: {conversion_type}")

    def _convert_to_word(self, uploaded_file):
        """Convert PDF to Word document"""
        temp_input = self.write_uploaded_file_to_temp(uploaded_file, '.pdf')
        temp_output = self.create_temp_file('.docx')

        try:
            cv = Converter(temp_input)
            cv.convert(temp_output)
            cv.close()

            with open(temp_output, 'rb') as f:
                docx_data = f.read()

            return {
                "type": "single_file",
                "message": "PDF converted to Word successfully!",
                "data": docx_data,
                "filename": f"{uploaded_file.name.replace('.pdf', '')}.docx",
                "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "button_label": "Download Word File"
            }
        finally:
            self.cleanup_temp_file(temp_input)
            self.cleanup_temp_file(temp_output)
