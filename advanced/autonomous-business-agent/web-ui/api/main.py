from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
from datetime import datetime
import shutil
from pathlib import Path

# Add parent directory to path to import agent modules
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.autonomous_agent import AutonomousAgent

app = FastAPI(title="Autonomous Business Agent API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002", "http://127.0.0.1:3002", "http://0.0.0.0:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define paths (BASE_DIR already defined above)
DATA_DIR = BASE_DIR / "data"
CHROMA_DB_DIR = BASE_DIR / "chroma_db"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str
    logs: list = []

class DocumentInfo(BaseModel):
    filename: str
    upload_date: str
    size: int

@app.get("/")
async def root():
    return {"message": "Autonomous Business Agent API", "status": "running"}

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    try:

        # Process the query using the autonomous agent
        agent = AutonomousAgent()

        result = await agent.run_async(request.query)

        # Create logs
        logs = [
            {
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "level": "info",
                "message": f"Query received: {request.query[:50]}..."
            },
            {
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "level": "info",
                "message": "Processing with RAG pipeline"
            },
            {
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "level": "success",
                "message": "Response generated successfully"
            }
        ]

        # Format logs from result
        formatted_logs = []
        for log in result["logs"]:
            formatted_logs.append({
                "timestamp": "",
                "level": "info",
                "message": log
            })

        return QueryResponse(
            response=result["result"],
            logs=formatted_logs
        )

    except Exception as e:
        import traceback
        traceback.print_exc() 
        
        logs = [
            {
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "level": "error",
                "message": f"Error processing query: {str(e)}"
            }
        ]
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents")
async def list_documents():
    """List all uploaded documents"""
    try:
        documents = []
        if DATA_DIR.exists():
            for file_path in DATA_DIR.glob("*.pdf"):
                stat = file_path.stat()
                documents.append({
                    "filename": file_path.name,
                    "upload_date": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "size": stat.st_size
                })
        return {"documents": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF document"""
    try:
        # Validate file type
        if not file.filename.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        # Save file
        file_path = DATA_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File uploaded successfully",
            "filename": file.filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/documents/{filename}")
async def delete_document(filename: str):
    """Delete a document"""
    try:
        file_path = DATA_DIR / filename
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="Document not found")

        file_path.unlink()
        return {"message": "Document deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rebuild-db")
async def rebuild_database():
    """Rebuild the vector database with all documents"""
    try:
        # Import the build_db function
        sys.path.append(str(BASE_DIR / "src"))
        from build_db import build_database

        # Rebuild the database
        build_database()

        return {"message": "Database rebuilt successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error rebuilding database: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
