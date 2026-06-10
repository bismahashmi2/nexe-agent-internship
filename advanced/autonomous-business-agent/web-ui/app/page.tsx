'use client'

import { useState } from 'react'
import ChatInterface from '@/components/ChatInterface'
import ExecutionLogs from '@/components/ExecutionLogs'
import DocumentManager from '@/components/DocumentManager'

export default function Home() {
  const [logs, setLogs] = useState<any[]>([])
  const [activeTab, setActiveTab] = useState<'chat' | 'documents'>('chat')

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-8">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-bold text-white mb-2">
            🤖 Autonomous Business Agent
          </h1>
          <p className="text-gray-300 text-lg">
            AI-powered multi-step reasoning with RAG pipeline
          </p>
        </div>

        {/* Tab Navigation */}
        <div className="flex justify-center mb-6">
          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-1 border border-white/20">
            <button
              onClick={() => setActiveTab('chat')}
              className={`px-6 py-2 rounded-lg font-semibold transition-all ${
                activeTab === 'chat'
                  ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white'
                  : 'text-gray-300 hover:text-white'
              }`}
            >
              💬 Chat
            </button>
            <button
              onClick={() => setActiveTab('documents')}
              className={`px-6 py-2 rounded-lg font-semibold transition-all ${
                activeTab === 'documents'
                  ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white'
                  : 'text-gray-300 hover:text-white'
              }`}
            >
              📄 Documents
            </button>
          </div>
        </div>

        {/* Content */}
        {activeTab === 'chat' ? (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <ChatInterface onLogsUpdate={setLogs} />
            </div>
            <div className="lg:col-span-1">
              <ExecutionLogs logs={logs} />
            </div>
          </div>
        ) : (
          <div className="max-w-4xl mx-auto">
            <DocumentManager />
          </div>
        )}
      </div>
    </main>
  )
}
