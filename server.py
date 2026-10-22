import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <-- Corrected capital 'M'
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from graph import bug_analyzer_app

app = FastAPI(title="AI Bug Report Analyzer API")

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BugRequest(BaseModel):
    description: str

@app.post("/api/analyze")
async def analyze_bug(request: BugRequest):
    if not request.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty.")
    
    initial_state = {
        "raw_description": request.description,
        "title": None,
        "affected_feature": None,
        "issue_summary": None,
        "severity": None,
        "root_causes": None,
        "formatted_report": None
    }
    
    try:
        final_state = bug_analyzer_app.invoke(initial_state)
        return {
            "title": final_state.get("title"),
            "affected_feature": final_state.get("affected_feature"),
            "severity": final_state.get("severity"),
            "issue_summary": final_state.get("issue_summary"),
            "root_causes": final_state.get("root_causes", []),
            "formatted_report": final_state.get("formatted_report")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static html files if index.html is in the same folder
@app.get("/")
async def read_root():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"message": "AI Bug Analyzer API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)