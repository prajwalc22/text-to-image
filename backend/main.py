import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allowing requests from the React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Hugging Face API URL and headers
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API key

# Define the input model for the prompt
class PromptInput(BaseModel):
    prompt: str

# Query function to call the Hugging Face API
def query(payload):
    logger.info(f"Sending request to Hugging Face API with payload: {payload}")
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        logger.info(f"Received response from Hugging Face API. Status code: {response.status_code}")
        return response.content
    except requests.Timeout:
        logger.error("Request to Hugging Face API timed out after 30 seconds")
        raise HTTPException(status_code=504, detail="Gateway Timeout: The image generation service is taking too long to respond")

# Endpoint to generate image from prompt
@app.post("/generate_image/")
async def generate_image(prompt_input: PromptInput):
    logger.info(f"Received prompt: {prompt_input.prompt}")
    try:
        image_bytes = query({"inputs": prompt_input.prompt})
        
        # Check if the response contains an error
        try:
            error_json = image_bytes.decode('utf-8')
            logger.error(f"Received error from Hugging Face API: {error_json}")
            raise HTTPException(status_code=500, detail=f"Error from image generation service: {error_json}")
        except UnicodeDecodeError:
            img_str = base64.b64encode(image_bytes).decode("utf-8")
            logger.info(f"Converted image to base64. Length: {len(img_str)}")
            return {"image_data": img_str}
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

