import os
from pypdf import PdfReader, PdfWriter

INPUT_DIR = "pdfs"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

folders = sorted([
    f for f in os.listdir(INPUT_DIR)
    if os.path.isdir(os.path.join(INPUT_DIR, f))
])

for folder in folders:
    folder_path = os.path.join(INPUT_DIR, folder)

    pdf_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ])

    if not pdf_files:
        print(f"⚠️ {folder} kosong, dilewati")
        continue

    writer = PdfWriter()

    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            writer.add_page(page)

    output_file = os.path.join(OUTPUT_DIR, f"{folder}.pdf")
    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"✅ Berhasil gabung: {output_file}")
