# PDFSense 📘

A comprehensive PDF management and conversion tool built with Streamlit. Transform, split, merge, and compress your PDF files with ease through an intuitive web interface.

## ✨ Features

### 🔁 PDF Conversion
- **PDF to Word (.docx)** - Convert PDF documents to editable Word format
- **PDF to PNG Images** - Extract pages as high-quality PNG images
- **PDF to Text** - Extract text content from PDF documents

### ✂️ PDF Splitting
- Extract specific page ranges from PDF documents
- Create multiple smaller files from large PDFs
- Flexible page selection with preview

### ➕ PDF Merging
- Combine multiple PDF files into a single document
- Maintain original quality and formatting
- Custom file ordering support

### 🗜️ PDF Compression
- Reduce file size while maintaining readability
- Multiple compression levels (Low, Medium, High)
- Real-time size reduction metrics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pdfsense.git
   cd pdfsense
Create a virtual environment (recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the application

bash
Copy
Edit
streamlit run main.py
Open your browser and navigate to http://localhost:8501

🏗️ Project Structure
bash
Copy
Edit
pdfsense/
├── main.py                    # Application entry point
├── config/
│   └── app_config.py         # Configuration settings
├── ui/
│   └── layout.py             # UI components and layouts
├── controllers/
│   └── pdf_controller.py     # Main application logic
├── services/
│   ├── base_service.py       # Base service class
│   ├── pdf_converter.py     # PDF conversion services
│   ├── pdf_splitter.py      # PDF splitting services
│   ├── pdf_merger.py        # PDF merging services
│   └── pdf_compressor.py    # PDF compression services
├── utils/
│   ├── session_manager.py   # Session state management
│   ├── file_validator.py    # File validation utilities
│   └── error_handler.py     # Error handling utilities
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
🛠️ Technology Stack
Frontend: Streamlit - Modern web app framework for Python

PDF Processing:

PyPDF2 - PDF manipulation and merging

PyMuPDF (fitz) - PDF compression and advanced operations

pdf2image - PDF to image conversion

pdf2docx - PDF to Word conversion

pdfminer.six - Text extraction

Image Processing: Pillow - Image manipulation and format conversion

📋 Requirements
txt
Copy
Edit
streamlit>=1.28.0
PyPDF2>=3.0.0
pdf2image>=1.16.0
pdf2docx>=0.5.6
PyMuPDF>=1.23.0
pdfminer.six>=20221105
Pillow>=9.0.0
🎯 Usage Examples
Converting PDF to Word
Select "Convert PDF" from the sidebar

Upload your PDF file

Choose "PDF to Word (.docx)" from the conversion options

Click "Convert File" and download the result

Splitting a PDF
Select "Split PDF" from the sidebar

Upload your PDF file

Specify the page range (start and end pages)

Click "Split PDF" and download the extracted pages

Merging Multiple PDFs
Select "Merge PDFs" from the sidebar

Upload multiple PDF files

Review the file order

Click "Merge PDFs" and download the combined document

Compressing a PDF
Select "Compress PDF" from the sidebar

Upload your PDF file

Choose compression level (Low/Medium/High)

Click "Compress PDF" and download the optimized file

🔧 Configuration
The application can be configured through config/app_config.py:

Compression Levels: Adjust quality and DPI settings

Supported Formats: Modify accepted file types

UI Settings: Customize app title, icon, and layout

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Guidelines
Follow PEP 8 style guidelines

Add appropriate error handling

Include docstrings for new functions

Test your changes thoroughly

Update documentation as needed

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🚀 Deployment
Local Development
bash
Copy
Edit
streamlit run main.py
Docker Deployment
dockerfile
Copy
Edit
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
Streamlit Cloud
Fork this repository

Connect your GitHub account to Streamlit Cloud

Deploy directly from your repository

📊 Performance Notes
Large PDF files may take longer to process

Image conversion requires sufficient memory

Compression results vary based on PDF content

Processing time scales with file size and complexity

🔒 Security Considerations
Files are processed locally and temporarily

No data is stored permanently on the server

Temporary files are automatically cleaned up

Consider file size limits for production deployment

📈 Future Enhancements
 Password-protected PDF support

 Batch processing capabilities

 OCR text extraction

 PDF metadata editing

 Custom compression algorithms

 API endpoint support

 Multiple language support



All open-source libraries that make this project possible

Made with ❤️ and Python
Built by Arideep Kanshabanik