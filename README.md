# 💰 Smart AI Budget Assistant

AI-powered personal finance management made simple using **Streamlit + Groq LLM**.

---

## 🚀 Project Overview

The **Smart AI Budget Assistant** is a web-based application that helps users manage their personal finances efficiently.
It analyzes financial data and provides **AI-driven insights** for budgeting, saving, and expense tracking.

---

## ✨ Features

### 📊 Budget Analysis

* Analyze income and expenses
* Get personalized financial advice
* Identify savings opportunities

### 📝 Expense Tracking

* Add and track daily expenses
* Categorize spending
* Analyze spending patterns

### 📁 File Upload Analysis

* Upload CSV or Excel files
* Automatic data processing using Pandas
* AI-generated insights from financial data

---

## 🧠 AI Integration

* Uses **Groq API (LLaMA model)**
* Generates **real-time financial advice**
* Provides **data-driven recommendations**

---

## ⚙️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **AI Model:** Groq (LLaMA 3)
* **Data Processing:** Pandas
* **File Handling:** OpenPyXL

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Smart_AI_Budget
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

**Windows**

```bash
myenv\Scripts\activate
```

**Mac/Linux**

```bash
source myenv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🔐 Security

* API keys are stored securely using `.env`
* `.env` is excluded via `.gitignore`
* No sensitive data is stored permanently

---

## 🧪 How It Works

1. User inputs financial data or uploads a file
2. Data is processed using **Pandas**
3. Structured prompt is sent to **Groq LLM**
4. AI generates financial recommendations
5. Results are displayed in the UI

---
---
## 🙌 Acknowledgements

* Groq AI
* Streamlit
* Pandas

---
