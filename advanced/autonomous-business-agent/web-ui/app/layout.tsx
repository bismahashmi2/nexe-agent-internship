import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Autonomous Business Agent',
  description: 'AI-powered autonomous agent system with RAG',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
