# Resume ATS Tracking LLM | Google Gemini

An AI-powered Resume ATS Tracking and Evaluation application built using **Python, Streamlit, and Google's Gemini API**. The application analyzes resumes against job descriptions, evaluates their relevance, identifies matching and missing skills, and generates AI-powered recommendations to improve resume quality.

## 🚀 Project Overview

Applicant Tracking Systems (ATS) are widely used by organizations to screen and shortlist candidates based on job requirements and resume content.

This project aims to simplify the resume evaluation process using Large Language Models (LLMs). Users can upload their resumes in PDF format and provide a job description. The application extracts resume content and uses Google Gemini to generate an AI-powered evaluation.

## ✨ Key Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Job Description Analysis:** Enter the target job description for evaluation.
- **ATS Compatibility Evaluation:** Analyze the relevance of the resume against the job requirements.
- **Resume Match Score:** Generate an AI-based resume matching percentage.
- **Skill Gap Analysis:** Identify matching skills and missing skills.
- **AI-Powered Recommendations:** Generate suggestions to improve resume content and job relevance.
- **LLM Integration:** Use Google's Gemini API for intelligent resume analysis.
- **Interactive Interface:** Simple and user-friendly interface developed with Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10 | Core programming language |
| Streamlit | Web application interface |
| Google Gemini API | AI-powered resume evaluation |
| Google Gen AI SDK | Gemini API integration |
| PyPDF2 | Extract text from PDF resumes |
| python-dotenv | Secure environment variable management |

## ⚙️ How It Works

1. The user uploads a resume in PDF format.
2. PyPDF2 extracts the textual content from the uploaded resume.
3. The user provides a job description.
4. The application prepares a prompt containing the resume content and job description.
5. Google Gemini processes the prompt and evaluates the resume.
6. The application displays the generated ATS evaluation, matching skills, missing skills, and improvement recommendations.

## 📂 Project Structure

```text
ResumeAts/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
├── .env                   # API key configuration (not uploaded)
├── .env.example           # Example environment configuration
│
└── .venv/                 # Python virtual environment (not uploaded)
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/codexsaswata/ResumeAts.git
```

### 2. Navigate to the Project Directory

```bash
cd ResumeAts
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## 🔑 Google Gemini API Configuration

The application requires a Google Gemini API key.

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Generate a Gemini API key.
3. Create a `.env` file in the project root directory.
4. Add your API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

**Important:** Never upload your actual `.env` file or API key to GitHub.

## ▶️ Run the Application

After completing the setup, execute:

```bash
streamlit run app.py
```

The application will start locally. Open the localhost URL displayed in your terminal to access the application.

## 📊 Application Workflow

**Input:**
- Resume (PDF format)
- Target job description

**Processing:**
- PDF text extraction
- Resume and job description analysis
- Gemini-powered evaluation

**Output:**
- ATS evaluation
- Resume match percentage
- Matching skills
- Missing skills
- AI-generated improvement suggestions

## 🔮 Future Enhancements

- Support for DOCX resume uploads.
- Resume keyword extraction and analysis.
- Detailed section-wise resume evaluation.
- Resume improvement and rewriting recommendations.
- Downloadable ATS evaluation reports.
- Resume comparison across multiple job descriptions.
- Deployment using Streamlit Community Cloud.

## ⚠️ Disclaimer

The generated ATS score and recommendations are AI-based estimates intended to assist candidates in improving their resumes. They do not represent the actual scoring system or shortlisting decision of any specific company's Applicant Tracking System.

## 👨‍💻 Author

**Saswata Pati**

- GitHub: [@codexsaswata](https://github.com/codexsaswata)

---

⭐ If you find this project useful, consider giving the repository a star!