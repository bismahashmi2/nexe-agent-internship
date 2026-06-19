'use client'

interface Log {
  timestamp: string
  level: string
  message: string
}

interface ExecutionLogsProps {
  logs: Log[]
}

export default function ExecutionLogs({ logs }: ExecutionLogsProps) {
  return (
    <div className="bg-white/10 backdrop-blur-lg rounded-2xl shadow-2xl border border-white/20 overflow-hidden h-[calc(100vh-200px)]">
      <div className="bg-gradient-to-r from-blue-700 to-blue-600 p-4">
        <h2 className="text-2xl font-bold text-white">Execution Logs</h2>
        <p className="text-white/80 text-sm">Real-time agent activity</p>
      </div>

      <div className="h-[calc(100%-80px)] overflow-y-auto p-4 space-y-2 font-mono text-sm">
        {logs.length === 0 ? (
          <div className="text-center text-gray-400 mt-20">
            <p>📋 No logs yet</p>
            <p className="text-xs mt-2">Logs will appear here when the agent processes queries</p>
          </div>
        ) : (
          logs.map((log, index) => (
            <div
              key={index}
              className={`p-3 rounded-lg border ${
                log.level === 'error'
                  ? 'bg-red-500/20 border-red-500/50 text-red-200'
                  : log.level === 'warning'
                  ? 'bg-yellow-500/20 border-yellow-500/50 text-yellow-200'
                  : 'bg-white/10 border-white/20 text-gray-200'
              }`}
            >
              <div className="flex items-start space-x-2">
                <span className="text-xs opacity-70">{log.timestamp}</span>
                <span className="font-semibold uppercase text-xs">
                  [{log.level}]
                </span>
              </div>
              <p className="mt-1 text-xs">{log.message}</p>
            </div>
          ))
        )}
      </div>
    </div>
  )
}
