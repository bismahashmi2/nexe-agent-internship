import sqlite3
from datetime import datetime
from agents import function_tool

DB_PATH = "src/database/app.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@function_tool
def save_search_query(query: str) -> dict:
    """
    Saves a search query to the database with a timestamp
    """
    try:
        init_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        timestamp = datetime.now().isoformat()
        cursor.execute('''
            INSERT INTO search_history (query, timestamp) VALUES (?, ?)
        ''', (query, timestamp))

        conn.commit()
        conn.close()
        
        print("Save search query tool fired ---->")
        return {
          "status": "success",
          "tool": "save_search_query",
          "message": "Query saved successfully",
          "query": query,
          "timestamp": timestamp
         }
        
    except Exception as e:
      return {
        "status": "error",
        "tool": "save_search_query",
        "query": query,
        "message": str(e)
     }