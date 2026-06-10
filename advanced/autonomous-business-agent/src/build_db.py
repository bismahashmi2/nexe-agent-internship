from read_pdf import extract_text
from chunk_text import chunk_text
from embeddings import get_embeddings
from vector_store import store_in_chroma
import os
from pathlib import Path

def build_database():
    """Build vector database from all PDFs in data directory"""
    data_dir = Path(__file__).parent.parent / "data"

    if not data_dir.exists():
        print("❌ Data directory not found!")
        return

    # Get all PDF files
    pdf_files = list(data_dir.glob("*.pdf"))

    if not pdf_files:
        print("⚠️ No PDF files found in data directory!")
        return

    print(f"📚 Found {len(pdf_files)} PDF file(s)")

    all_chunks = []

    for pdf_path in pdf_files:
        print(f"\n📄 Processing: {pdf_path.name}")

        try:
            # Extract text
            text = extract_text(str(pdf_path))

            # Chunk text
            chunks = chunk_text(text)
            print(f"  ✂ Created {len(chunks)} chunks")

            # Add filename metadata to chunks
            chunks_with_metadata = [
                f"[Source: {pdf_path.name}] {chunk}"
                for chunk in chunks
            ]

            all_chunks.extend(chunks_with_metadata)

        except Exception as e:
            print(f"  ❌ Error processing {pdf_path.name}: {str(e)}")
            continue

    if not all_chunks:
        print("\n❌ No chunks created!")
        return

    print(f"\n🧠 Creating embeddings for {len(all_chunks)} total chunks...")
    embeddings = get_embeddings(all_chunks)

    print("💾 Storing in ChromaDB...")
    store_in_chroma(all_chunks, embeddings)

    print("✅ DONE: Vector DB is ready!")

if __name__ == "__main__":
    build_database()