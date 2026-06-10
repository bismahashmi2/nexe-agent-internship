# User Guide: Document Upload & Management

## 🎯 Complete User Interaction Flow

### Step 1: Access the Web Interface

1. Start the application (from WSL):
```bash
cd /mnt/d/Code/Agentic\ AI/Internship\ Tasks/nexe-agent-internship/advanced/autonomous-business-agent/web-ui
./start.sh
```

2. Open your Windows browser and go to: `http://localhost:3002`

### Step 2: Upload Documents

1. Click on the **"📄 Documents"** tab at the top
2. You'll see the Document Manager interface
3. Click on the upload area or drag & drop a PDF file
4. Wait for:
   - **Upload Progress**: File is being uploaded to the server
   - **Processing**: Vector database is being rebuilt with embeddings
5. You'll see a success message when complete

### Step 3: View Uploaded Documents

- All uploaded documents are listed in the Document Manager
- Each document shows:
  - Filename
  - Upload date
  - File size
- Click **🔄 Refresh** to update the list

### Step 4: Chat with the Agent

1. Click on the **"💬 Chat"** tab
2. Type your question in the chat input
3. The agent will:
   - Search through ALL uploaded documents
   - Retrieve relevant context
   - Generate an intelligent response
4. View execution logs in the right panel

### Step 5: Delete Documents (Optional)

1. Go to the **"📄 Documents"** tab
2. Click **🗑️ Delete** next to any document
3. Confirm the deletion
4. The vector database will automatically rebuild

---

## 🔄 How It Works Behind the Scenes

### Document Upload Process:

```
User uploads PDF
    ↓
File saved to data/ folder
    ↓
PDF text extracted
    ↓
Text split into chunks
    ↓
Chunks converted to embeddings
    ↓
Embeddings stored in ChromaDB
    ↓
Ready for queries!
```

### Query Process:

```
User asks question
    ↓
Question converted to embedding
    ↓
Similar chunks retrieved from ChromaDB
    ↓
Context + Question sent to LLM
    ↓
LLM generates answer
    ↓
Response displayed to user
```

---

## 📋 Features

### ✅ What You Can Do:

- **Upload PDFs**: Add business documents, reports, manuals, etc.
- **Multiple Documents**: Upload as many PDFs as you need
- **Automatic Processing**: Vector database rebuilds automatically
- **Smart Search**: Agent searches across all documents
- **Real-time Chat**: Ask questions and get instant answers
- **Execution Logs**: See what the agent is doing in real-time
- **Document Management**: View and delete documents anytime

### 🎨 User Interface:

- **Chat Tab**:
  - Real-time messaging interface
  - Message history
  - Loading indicators
  - Execution logs panel

- **Documents Tab**:
  - Drag & drop upload
  - Upload progress bar
  - Document list with metadata
  - Delete functionality

---

## 💡 Example Use Cases

### Business Intelligence:
1. Upload quarterly reports
2. Ask: "What was our revenue growth in Q1?"
3. Get answers with context from your documents

### Technical Documentation:
1. Upload API documentation
2. Ask: "How do I authenticate with the API?"
3. Get specific instructions from your docs

### Policy & Compliance:
1. Upload company policies
2. Ask: "What is the remote work policy?"
3. Get accurate policy information

---

## 🚨 Important Notes

### File Requirements:
- **Format**: PDF only
- **Size**: No strict limit (but larger files take longer to process)
- **Content**: Text-based PDFs work best (scanned images may not work well)

### Processing Time:
- **Small PDFs** (< 10 pages): ~5-10 seconds
- **Medium PDFs** (10-50 pages): ~15-30 seconds
- **Large PDFs** (50+ pages): ~1-2 minutes

### Database Rebuilding:
- Happens automatically after upload/delete
- All documents are reprocessed together
- Ensures consistency across the knowledge base

---

## 🔧 Troubleshooting

### Upload Fails:
- Check file is a valid PDF
- Ensure backend server is running
- Check browser console for errors

### No Response from Agent:
- Make sure at least one document is uploaded
- Check that vector database was built successfully
- Verify backend logs for errors

### Slow Processing:
- Large PDFs take time to process
- Multiple documents increase processing time
- This is normal - wait for completion

---

## 🎯 Best Practices

1. **Organize Documents**: Upload related documents together
2. **Clear Naming**: Use descriptive filenames
3. **Regular Updates**: Delete outdated documents
4. **Test Queries**: Try different questions to see what works best
5. **Monitor Logs**: Check execution logs for insights

---

## 📊 System Status Indicators

- **Green Messages**: Success (upload complete, query processed)
- **Red Messages**: Error (upload failed, processing error)
- **Loading Animations**: Processing in progress
- **Progress Bars**: Upload/processing status

---

## 🎉 You're Ready!

The system is now fully functional with:
- ✅ Document upload capability
- ✅ Automatic vector database management
- ✅ Multi-document support
- ✅ Real-time chat interface
- ✅ Execution monitoring
- ✅ Document management

Start by uploading your first PDF and asking questions!
