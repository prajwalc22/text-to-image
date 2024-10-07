# How to Use the Text-to-Image Generator

Follow these steps to set up and run the Text-to-Image Generator application:

## Step 1: Clone the Repository


## Step 2: Set Up the Backend

1. Navigate to the backend directory:

2. Install the required Python packages:

```pip install fastapi uvicorn requests Pillow```


3. Open `main.py` and replace `YOUR_HUGGINGFACE_API_KEY` with your actual Hugging Face API key.

## Step 3: Run the Backend Server

In the backend directory, start the FastAPI server with the following command:

`uvicorn main:app --reload`


The server will start at `http://127.0.0.1:8000`.

## Step 4: Set Up the Frontend

1. Navigate to the frontend directory


2. Install dependencies using bun:
 `bun install`

 
## Step 5: Run the Frontend Application

In the frontend directory, start the React application with the following command:
``bun dev``

The frontend will be available at `http://localhost:5173`.

## Step 6: Generate Images

1. Open your browser and go to `http://localhost:5173`.
2. Enter your text prompt in the input field and click "Generate Image".
3. The generated image will be displayed below the input form.

## Additional Notes

- Ensure both the backend and frontend servers are running for the application to function properly.
- If you encounter a timeout issue while generating images, consider increasing the timeout in the `main.py` file.






