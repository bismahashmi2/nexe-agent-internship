from pypdf import PdfReader

pdf_path = "data/ai_dev.pdf"

reader = PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

first_page = reader.pages[0]

text = first_page.extract_text()

print(text)