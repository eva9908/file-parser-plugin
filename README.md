# file-parser-plugin
A FastAPI plugin to parse PDF, Word, Excel, and TXT files into structured/unstructured data for LLM-friendly content extraction.
# File Parser Plugin for Coze

## 🚀 Introduction

This is a FastAPI-based plugin designed to work with the Coze platform. It helps extract structured and unstructured data from various file formats, such as PDFs, Word documents, Excel files, and plain text files. The extracted content is processed to facilitate better intent recognition by LLMs (Large Language Models).

---

## 🧩 Features

- **Multi-format support**: Handles PDF, Word (.docx), Excel (.xlsx), and plain text (.txt) files.
- **Content extraction**: Extracts both structured and unstructured data, ready for LLM consumption.
- **Named Entity Recognition (NER)**: Key entities and keywords are extracted for better content understanding.
- **FastAPI-powered**: Lightweight, fast, and easy to deploy.
- **RESTful API**: Expose the plugin as an API for integration with other platforms.

---

## 🚀 Quick Start Guide

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-parser-plugin.git
cd file-parser-plugin
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
curl -X POST http://localhost:10000/upload/ -F "file=@yourfile.pdf"
file_parser_plugin/
├── main.py               # FastAPI application entry point
├── requirements.txt      # List of dependencies
├── openapi_plugin.json   # Coze plugin configuration file
└── utils/                # Utility scripts for parsing various file formats
    ├── parser_pdf.py     # PDF file parsing logic
    ├── parser_docx.py    # Word document parsing logic
    ├── parser_excel.py   # Excel file parsing logic
    ├── parser_txt.py     # Plain text parsing logic
    └── keyword_ner.py    # Keyword extraction and NER logic


---

### 📋 使用方法：

1. 复制上述内容到一个新的 `README.md` 文件中。
2. 这个文件将帮助其他开发者快速理解插件的功能、安装步骤和如何使用 API。

---

现在，你可以将这个新的 `README.md` 文件上传到你的 GitHub 仓库！如果有其他问题或需要进一步修改，告诉我！
