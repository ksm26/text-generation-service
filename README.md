# 📝 Text Generation API

A simple text generation service that uses a pretrained LLM (Hugging Face Transformers model).
This API takes a short prompt as input and returns a generated text passage.

---

## 🚀 Features

✅ **Pretrained LLM**: Uses an open-source model from Hugging Face. \
✅ **REST API**: Accepts a prompt and returns generated text. \
✅ **Dockerized**: Runs in a container for easy deployment. \
✅ **FastAPI Framework**: Provides a lightweight and efficient backend.

---

## 📂 Project Structure

text_generation_service/ \
│── backend/               # FastAPI backend  
│   ├── main.py           # API implementation  
│   ├── model.py          # LLM loading & inference  
│   ├── requirements.txt  # Backend dependencies  
│── Dockerfile            # Docker container setup  
│── README.md             # Documentation  

---

## 🛠️ Tech Stack  

| Component  | Technology Used  |
|------------|----------------|
| **Backend** | FastAPI, Transformers (Hugging Face) |
| **Containerization** | Docker |
| **Model** | GPT-2 (or any Hugging Face model) |

---

## 🚀 Setup Instructions  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/text_generation_service.git
cd text_generation_service
```

### **2️⃣ Install Dependencies**  
```sh
cd backend
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**  
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **4️⃣ Start the Backend**  

The API will be available at: http://localhost:8000

## 🐳 Docker Deployment

### 1️⃣ Build the Docker Image
```sh
docker build -t text-generation-service .
```

### 2️⃣ Run the Docker Container
```sh
docker run -p 8080:8000 text-generation-service
```

The API will be available at: http://localhost:8080


## 🌍 Usage

### Submit a Prompt
```sh
curl -X POST "http://127.0.0.1:8080/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Once upon a time,"}'
```

### 📌 Expected Response:
```sh
{"generated_text": "Once upon a time, in a distant kingdom..."}
```
