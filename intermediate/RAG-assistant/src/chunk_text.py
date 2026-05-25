from pypdf import PdfReader

pdf_path = "data/ai_dev.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        full_text += text + "\n"
print("Text extracted successfully.")
print()

CHUNK_SIZE = 500

chunks = []

for i in range(0, len(full_text), CHUNK_SIZE):
    chunk = full_text[i : i + CHUNK_SIZE]
    chunks.append(chunk)

print(f"Total chunks created: {len(chunks)}")    
print()

print("First Chunk:")
print()
print(chunks[0])