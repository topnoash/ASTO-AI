# 🤖 ASTO AI — Multimodal AI Assistant

<p align="center">
  <b>An AI-powered multimodal assistant capable of understanding text, PDFs, and images using modern Generative AI models.</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)
![AI](https://img.shields.io/badge/AI-Generative_AI-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</p>


## 🚀 Overview

**ASTO AI** is a lightweight multimodal AI assistant that combines Large Language Models, computer vision, and document intelligence into a single interactive application.

The system allows users to:

- 💬 Chat with an AI assistant
- 📄 Upload and analyze PDF documents
- 🔍 Extract information from scanned documents using OCR
- 🖼️ Understand and interact with images
- 🧠 Ask context-based questions from uploaded content


The goal of ASTO AI is to provide a unified AI workspace where users can interact with different types of information through natural language.


---

# ✨ Features


## 💬 AI Chat Assistant

- General-purpose conversational AI
- Context-aware responses
- Powered by OpenAI-compatible APIs through OpenRouter


---

## 📄 Intelligent PDF Assistant

ASTO AI supports both digital and scanned PDF documents.

### Capabilities:

✅ PDF text extraction  
✅ Automatic document processing  
✅ PDF summarization  
✅ Question answering from documents  
✅ OCR support for image-based PDFs  


### Pipeline

```
PDF Upload
     |
     |
PyMuPDF Extraction
     |
     |
Text Available?
     |
 ┌───┴────┐
Yes       No
 |         |
Text     EasyOCR
 |         |
 └───┬────┘
     |
AI Processing
     |
Response
```


---

## 🖼️ Vision AI Assistant

The image assistant enables users to interact with images.

### Capabilities:

- Upload images
- Generate image descriptions
- Ask questions about images
- Analyze visual content using vision models


Example:

```
User:
"What is happening in this image?"

AI:
Provides a detailed visual explanation.
```


---

# 🏗️ System Architecture


```
                 User
                  |
                  |
            Streamlit UI
                  |
        --------------------
        |                  |
     Chat Module      File Processing
        |                  |
        |             -------------
        |             |           |
     LLM API       PDF         Images
        |             |           |
        |          PyMuPDF     Vision AI
        |             |
        |          EasyOCR
        |
     Response Generation
```


---

# 🛠️ Tech Stack


## Programming Language

- Python


## Frontend

- Streamlit


## AI & LLM

- OpenAI SDK
- OpenRouter API
- Vision-capable Generative AI Models


## Document Intelligence

- PyMuPDF
- EasyOCR


## Image Processing

- Pillow
- NumPy


---

# 📂 Project Structure


```
ASTO-multimodal-ai-assistant/

│
├── app.py
│
├── image/
│   ├── image_assistant.py
│   └── image_utils.py
│
├── pdf/
│   └── pdf_utils.py
│
├── requirements.txt
│
├── .env.example
│
└── LICENSE

```


---

# ⚙️ Installation


## 1. Clone Repository


```bash
git clone https://github.com/topnoash/ASTO-AI.git

cd ASTO-AI
```


---

## 2. Create Virtual Environment


```bash
python -m venv venv
```


Activate:


### Windows

```bash
venv\Scripts\activate
```


### Linux/Mac

```bash
source venv/bin/activate
```


---

## 3. Install Dependencies


```bash
pip install -r requirements.txt
```


---

# 🔑 Environment Configuration


Create a `.env` file:


```
OPENROUTER_API_KEY=your_api_key_here
```


You can get your API key from:

https://openrouter.ai/


---

# ▶️ Running The Application


Start Streamlit:


```bash
streamlit run app.py
```


Application will start at:


```
http://localhost:8501
```


---

# 📸 Screenshots


Add screenshots here:

```
assets/
 ├── chat.png
 ├── pdf-analysis.png
 └── image-analysis.png
```


---

# 🔮 Future Improvements


Planned enhancements:

- [ ] Retrieval Augmented Generation (RAG)
- [ ] Vector database integration
- [ ] Long-term conversation memory
- [ ] Multiple document support
- [ ] User authentication
- [ ] Cloud deployment
- [ ] Voice interaction
- [ ] Advanced multimodal agents


---

# 🧠 Learning Outcomes


This project demonstrates practical implementation of:

- Generative AI applications
- Multimodal AI systems
- Document intelligence pipelines
- OCR integration
- Vision-language models
- API-based AI architectures


---

# 🤝 Contributing


Contributions are welcome!


Steps:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature/new-feature
```

5. Open a Pull Request


---

# 📄 License


This project is licensed under the MIT License.


---

# 👨‍💻 Author


**Topno Ash**

GitHub:
https://github.com/topnoash


---

<p align="center">
Built with ❤️ using Generative AI
</p>
