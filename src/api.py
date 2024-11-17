from fastapi import FastAPI, UploadFile, File
import pandas as pd
from summarizer import summarize_performance
from feedback_generator import generate_feedback

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a CSV file and process it.
    Args:
        file (UploadFile): Uploaded CSV file.
    Returns:
        dict: Summary and feedback for the uploaded data.
    """
    try:
        contents = await file.read()
        data = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))
        summary = summarize_performance(data)
        feedback = generate_feedback(data)
        return {"summary": summary.to_dict(), "feedback": feedback}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

