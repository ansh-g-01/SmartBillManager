
# Smart Bill Manager

SmartBill Manager is an AI-powered invoice management system that automates the process of reading, storing, and following up on bills. It uses OCR and LLMs to extract structured data from scanned bills or uploaded images and enables email reminders for pending payments. Designed for small businesses, freelancers, and anyone looking to simplify invoice tracking.


## Installation

Install my-project with npm

```bash
  git clone https://github.com/your-username/smartbill-manager
  cd smartbill-manager
  pip install -r requirements.txt
```
    
## Usage/Examples


```bash
  streamlit run app.py

```

Typical flow:

1.Upload a scanned bill or invoice.

2.OCR + LLM extract fields like name, amount, email, and due date.

3.View extracted data in a structured UI.

4.Mark as paid or leave as unpaid.

5.Email reminders are sent for unpaid bills.
## Tech Stack

**Language**: Python

**OCR Engine**: Tesseract OCR

**LLM**: Groq / Ollama

**Database**: SQLite

**UI Framework**: Streamlit

**Email Automation**: smtplib



## FAQ

### 1. Why did you use streamlit?

Answer :  Streamlit is extremely useful for rapid development and prototyping. Since the core focus of this project was on showcasing the concept (OCR + LLM-powered automation) rather than frontend complexity, Streamlit allowed me to quickly build an interactive UI with minimal effort.

### 2. Why SQlite , why not others like Postgre or MySql?

Answer : I chose SQLite because I plan to eventually extend this project to mobile platforms. SQLite is lightweight, file-based, and serverless, making it ideal for embedding into apps without the need for external database servers. This helps keep the entire system self-contained and easy to deploy anywhere.

### 3. Do I need internet for LLM parsing?
Answer : Yes, if you're using Groq or OpenRouter for LLM parsing. For full offline functionality, replace it with a local model.

### 4. What kinds of bills does this support?
Answer: SmartBill Manager works best with scanned or clear images of printed invoices, especially those with standard structure (vendor name, amount, due date, etc.).

### 5. Is this production-ready?
It’s a proof-of-concept. For production, add authentication, PDF export, error logging, and better OCR tuning.
