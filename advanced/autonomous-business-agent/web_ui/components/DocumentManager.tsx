'use client'

import { useState } from 'react'
import axios from 'axios'

interface Document {
  filename: string
  upload_date: string
  size: number
}

export default function DocumentManager() {
  const [documents, setDocuments] = useState<Document[]>([])
  const [uploading, setUploading] = useState(false)
  const [processing, setProcessing] = useState(false)
  const [uploadProgress, setUploadProgress] = useState(0)
  const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null)

  const fetchDocuments = async () => {
    try {
      const response = await axios.get('http://localhost:8000/documents')
      setDocuments(response.data.documents)
    } catch (error) {
      console.error('Error fetching documents:', error)
    }
  }

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    if (!file.name.endsWith('.pdf')) {
      setMessage({ type: 'error', text: 'Only PDF files are supported' })
      return
    }

    setUploading(true)
    setMessage(null)
    setUploadProgress(0)

    const formData = new FormData()
    formData.append('file', file)

    try {
      // Upload file
      await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          const progress = progressEvent.total
            ? Math.round((progressEvent.loaded * 100) / progressEvent.total)
            : 0
          setUploadProgress(progress)
        }
      })

      setMessage({ type: 'success', text: 'File uploaded successfully!' })
      setUploading(false)
      setProcessing(true)

      // Process document and rebuild database
      await axios.post('http://localhost:8000/rebuild-db')

      setProcessing(false)
      setMessage({ type: 'success', text: 'Document processed and added to knowledge base!' })

      // Refresh document list
      await fetchDocuments()

      // Clear file input
      event.target.value = ''
    } catch (error: any) {
      setUploading(false)
      setProcessing(false)
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Error uploading file'
      })
    }
  }

  const handleDeleteDocument = async (filename: string) => {
    if (!confirm(`Are you sure you want to delete ${filename}?`)) return

    try {
      await axios.delete(`http://localhost:8000/documents/${filename}`)
      setMessage({ type: 'success', text: 'Document deleted successfully!' })

      // Rebuild database
      setProcessing(true)
      await axios.post('http://localhost:8000/rebuild-db')
      setProcessing(false)

      // Refresh document list
      await fetchDocuments()
    } catch (error: any) {
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Error deleting document'
      })
    }
  }

  // Fetch documents on component mount
  useState(() => {
    fetchDocuments()
  })

  return (
    <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl border border-white/20 overflow-hidden">
      <div className="bg-gradient-to-r from-blue-900 to-blue-700 p-4">
        <h2 className="text-2xl font-bold text-white">Document Manager</h2>
        <p className="text-white/80 text-sm">Upload and manage your knowledge base</p>
      </div>

      <div className="p-6 space-y-6">
        {/* Upload Section */}
        <div className="border-2 border-dashed border-white/30 rounded-xl p-6 text-center hover:border-blue-500/50 transition-colors">
          <input
            type="file"
            accept=".pdf"
            onChange={handleFileUpload}
            disabled={uploading || processing}
            className="hidden"
            id="file-upload"
          />
          <label
            htmlFor="file-upload"
            className={`cursor-pointer ${uploading || processing ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            <div className="space-y-2">
              <div className="text-4xl">📄</div>
              <p className="text-white font-semibold">
                {uploading ? 'Uploading...' : processing ? 'Processing...' : 'Click to upload PDF'}
              </p>
              <p className="text-gray-400 text-sm">
                PDF files only
              </p>
            </div>
          </label>

          {uploading && (
            <div className="mt-4">
              <div className="w-full bg-gray-700 rounded-full h-2">
                <div
                  className="bg-gradient-to-r from-blue-600 to-blue-400 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${uploadProgress}%` }}
                ></div>
              </div>
              <p className="text-white text-sm mt-2">{uploadProgress}%</p>
            </div>
          )}

          {processing && (
            <div className="mt-4">
              <div className="flex items-center justify-center space-x-2">
                <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce"></div>
                <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                <div className="w-3 h-3 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
              </div>
              <p className="text-white text-sm mt-2">Building vector database...</p>
            </div>
          )}
        </div>

        {/* Message */}
        {message && (
          <div className={`p-4 rounded-lg ${
            message.type === 'success'
              ? 'bg-green-500/20 border border-green-500/50 text-green-200'
              : 'bg-red-500/20 border border-red-500/50 text-red-200'
          }`}>
            {message.text}
          </div>
        )}

        {/* Documents List */}
        <div>
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-white">Uploaded Documents</h3>
            <button
              onClick={fetchDocuments}
              className="text-sm text-blue-400 hover:text-blue-300 transition-colors"
            >
              🔄 Refresh
            </button>
          </div>

          {documents.length === 0 ? (
            <div className="text-center text-gray-400 py-8">
              <p>No documents uploaded yet</p>
              <p className="text-sm mt-2">Upload a PDF to get started</p>
            </div>
          ) : (
            <div className="space-y-2">
              {documents.map((doc, index) => (
                <div
                  key={index}
                  className="flex items-center justify-between p-4 bg-white/5 rounded-lg border border-white/10 hover:border-blue-500/30 transition-colors"
                >
                  <div className="flex items-center space-x-3">
                    <span className="text-2xl">📄</span>
                    <div>
                      <p className="text-white font-medium">{doc.filename}</p>
                      <p className="text-gray-400 text-xs">
                        {new Date(doc.upload_date).toLocaleDateString()} • {(doc.size / 1024).toFixed(2)} KB
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => handleDeleteDocument(doc.filename)}
                    className="text-red-400 hover:text-red-300 transition-colors px-3 py-1 rounded-lg hover:bg-red-500/10"
                  >
                    🗑️ Delete
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
