# Autonomous Business Agent - Web UI

A modern web interface for the Autonomous Business Agent with RAG pipeline integration.

## Architecture

- **Frontend**: Next.js 14 with TypeScript and Tailwind CSS
- **Backend**: FastAPI server that interfaces with the Python agent
- **Port**: Frontend runs on `http://localhost:3002`
- **API**: Backend runs on `http://localhost:8000`

## Features

- 💬 Real-time chat interface with the autonomous agent
- 📊 Live execution logs and agent activity monitoring
- 🎨 Modern, responsive UI with gradient backgrounds
- 🔄 Seamless integration with RAG pipeline
- ⚡ Fast and efficient query processing
- 📄 **Document Upload & Management** - Upload PDFs directly through the UI
- 🗑️ **Document Deletion** - Remove documents and auto-rebuild database
- 📚 **Multi-Document Support** - Query across multiple uploaded documents
- 🔄 **Automatic Database Rebuilding** - Vector DB updates automatically

## Setup

### 1. Install Frontend Dependencies

```bash
cd web_ui
npm install
```

### 2. Install Backend Dependencies

```bash
cd web_ui/api
pip install -r requirements.txt
```

Or if using the parent project's virtual environment:

```bash
cd ../..
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install fastapi uvicorn pydantic python-multipart
```

## Running the Application

### Start the Backend API Server

```bash
# From the web_ui/api directory
python main.py
```

The API will be available at `http://localhost:8000`

### Start the Frontend Development Server

```bash
# From the web_ui directory
npm run dev
```

The web interface will be available at `http://localhost:3002`

## Usage

### Quick Start

1. Open your browser and navigate to `http://localhost:3002`
2. You'll see two tabs: **💬 Chat** and **📄 Documents**

### Upload Documents

1. Click on the **📄 Documents** tab
2. Click the upload area or drag & drop a PDF file
3. Wait for the upload and processing to complete
4. Your document is now in the knowledge base!

### Chat with the Agent

1. Click on the **💬 Chat** tab
2. Type your question in the chat input
3. The agent will search through all uploaded documents
4. View the response in the chat interface
5. Monitor execution logs in the right panel

### Manage Documents

1. Go to the **📄 Documents** tab
2. View all uploaded documents with metadata
3. Click **🗑️ Delete** to remove a document
4. The database automatically rebuilds after changes

For detailed instructions, see [USER_GUIDE.md](./USER_GUIDE.md)

## Building for Production

```bash
npm run build
npm start
```

## Project Structure

```
web_ui/
├── app/
│   ├── globals.css       # Global styles
│   ├── layout.tsx        # Root layout
│   └── page.tsx          # Home page with tabs
├── components/
│   ├── ChatInterface.tsx    # Chat UI component
│   ├── ExecutionLogs.tsx    # Logs display component
│   └── DocumentManager.tsx  # Document upload & management
├── api/
│   ├── main.py          # FastAPI backend
│   └── requirements.txt # Python dependencies
├── package.json
├── tsconfig.json
├── tailwind.config.js
├── next.config.js
├── USER_GUIDE.md        # Detailed user guide
└── WSL_WINDOWS_SETUP.md # WSL to Windows setup
```

## API Endpoints

### POST /query
Process a user query through the autonomous agent.

**Request:**
```json
{
  "query": "What is the revenue for Q1?"
}
```

**Response:**
```json
{
  "response": "Based on the documents...",
  "logs": [
    {
      "timestamp": "12:34:56",
      "level": "info",
      "message": "Query received"
    }
  ]
}
```

### GET /documents
List all uploaded documents.

**Response:**
```json
{
  "documents": [
    {
      "filename": "report.pdf",
      "upload_date": "2026-06-01T10:30:00",
      "size": 1024000
    }
  ]
}
```

### POST /upload
Upload a PDF document.

**Request:** Multipart form data with file

**Response:**
```json
{
  "message": "File uploaded successfully",
  "filename": "report.pdf"
}
```

### DELETE /documents/{filename}
Delete a document.

**Response:**
```json
{
  "message": "Document deleted successfully"
}
```

### POST /rebuild-db
Rebuild the vector database with all documents.

**Response:**
```json
{
  "message": "Database rebuilt successfully"
}
```

## Notes

- **No manual database setup required** - Upload documents through the UI
- Documents are automatically processed and added to the vector database
- The agent searches across all uploaded documents when answering queries
- Logs are displayed in real-time as the agent processes queries
- Supports multiple PDF documents simultaneously
- Database automatically rebuilds when documents are added or removed
- All documents are stored in the `data/` folder
- Vector embeddings are stored in `chroma_db/`
