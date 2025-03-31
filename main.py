# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import pipeline

# # Initialize FastAPI app
# app = FastAPI()

# # Load the text generation model (use a lightweight model for CPU)
# try:
#     text_generator = pipeline("text-generation", model="distilgpt2")
# except Exception as e:
#     text_generator = None
#     print(f"Error loading model: {e}")

# # Define request model
# class PromptRequest(BaseModel):
#     prompt: str

# @app.get("/")
# def root():
#     return {"message": "Welcome to the Text Generation API. Use /generate to get AI-generated text."}

# @app.post("/generate")
# def generate_text(request: PromptRequest):
#     if text_generator is None:
#         raise HTTPException(status_code=500, detail="Model failed to load. Check logs.")
    
#     try:
#         result = text_generator(request.prompt, max_length=200, num_return_sequences=1)
#         return {"generated_text": result[0]["generated_text"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the text generation model
text_generator = pipeline("text-generation", model="gpt2")

@app.get("/", response_class=HTMLResponse)
async def home_page():
    return """
    <html>
    <head>
        <title>Text Generation</title>
    </head>
    <body>
        <h2>Enter a prompt to generate text:</h2>
        <form action="/generate" method="post">
            <input type="text" name="prompt" required>
            <input type="submit" value="Generate">
        </form>
    </body>
    </html>
    """

@app.post("/generate", response_class=HTMLResponse)
async def generate_text(prompt: str = Form(...)):
    try:
        result = text_generator(prompt, max_length=200, num_return_sequences=1)
        generated_text = result[0]["generated_text"]
        return f"""
        <html>
        <head>
            <title>Generated Text</title>
        </head>
        <body>
            <h2>Generated Text:</h2>
            <p>{generated_text}</p>
            <a href="/">Go back</a>
        </body>
        </html>
        """
    except Exception as e:
        return f"Error: {str(e)}"
