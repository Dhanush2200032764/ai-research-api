# 🚀 AI Research Summary API

A simple REST API built using FastAPI that leverages Large Language Models (LLMs) to generate concise summaries from input text. This project demonstrates how AI can be integrated into backend services for automation and productivity.

---

## 📌 Features

* 🔹 RESTful API built with FastAPI
* 🔹 Accepts raw text input
* 🔹 Generates AI-powered summaries
* 🔹 Interactive API documentation (Swagger UI)
* 🔹 Easy deployment on cloud platforms

---

## 🧱 Tech Stack

* **Backend:** FastAPI (Python)
* **AI Integration:** Groq API / OpenAI-compatible API
* **HTTP Requests:** Requests
* **Deployment:** Render / Railway

---

## 📂 Project Structure

```
ai-research-api/
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-research-api.git
cd ai-research-api
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

Open your browser:
👉 http://127.0.0.1:8000/docs

---

## 🔌 API Endpoints

### 1. Health Check

```
GET /
```

**Response:**

```json
{
  "message": "AI Research Summary API is running"
}
```

---

### 2. Summarize Text

```
POST /summarize
```

**Request Body:**

```json
{
  "text": "Artificial Intelligence is transforming industries..."
}
```

**Response:**

```json
{
  "summary": "AI is revolutionizing industries by improving efficiency and automation..."
}
```

---

## 🔑 Environment Variables

Replace your API key in `main.py`:

```
YOUR_API_KEY=your_groq_or_openai_api_key
```

---

## ☁️ Deployment

### Render

* Connect your GitHub repository
* Build command:

  ```
  pip install -r requirements.txt
  ```
* Start command:

  ```
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```

---

## 🎯 Use Cases

* Research paper summarization
* Content generation tools
* AI-powered assistants
* Automation pipelines

---

## 🧪 Future Improvements

* 📄 PDF upload and summarization
* 🌐 URL-based content extraction
* 🧠 Keyword extraction
* 🔐 Authentication & rate limiting

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* FastAPI for the backend framework
* Groq/OpenAI for LLM capabilities
* MLH Global Hack Week for the challenge
