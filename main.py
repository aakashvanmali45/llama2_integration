from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) configuration to allow requests from your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add the origin of your React app
    allow_methods=["*"],
    allow_headers=["*"],
)
contents = ''
@app.post("/upload_files")
async def upload_files(file: UploadFile):
    try:
        # Read and decode the contents of the uploaded file into a string
        file_contents = file.file.read().decode("utf-8")

        # Determine the file type based on the file extension
        
        contents = file_contents
        return {"Success": "File Parsed Successfully"}
    
    except FileNotFoundError:
        return {"error": "File not found."}
    
    except UnicodeDecodeError:
        return {"error": "Unable to decode the file as UTF-8."}

    except Exception as e:
        return {"error": str(e)}


@app.post("/api/your-ml-endpoint")
async def question_answering(query: str = Form(...)):
    try:
        # Replace this with your actual machine learning model logic
        # Here, we're just echoing the question as an answer for demonstration purposes
        answer = query
        
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
