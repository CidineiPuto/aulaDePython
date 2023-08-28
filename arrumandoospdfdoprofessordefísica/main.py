from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / "pdfs"
NEW_FOLDER = PDF_FOLDER / "new_pdfs"
ORIGINAL_FOLDER = PDF_FOLDER / "original_pdf"
CAMSCANNER = ORIGINAL_FOLDER / "CamScanner.pdf"

NEW_FOLDER.mkdir(exist_ok=True)
reader_camscanner = PdfReader(CAMSCANNER)

page1 = reader_camscanner.pages[0]
page2 = reader_camscanner.pages[1]
page3 = reader_camscanner.pages[2]
page4 = reader_camscanner.pages[3]
page5 = reader_camscanner.pages[4]
page6 = reader_camscanner.pages[5]
page7 = reader_camscanner.pages[6]
page8 = reader_camscanner.pages[7]


# for i, page in enumerate(reader_camscanner.pages):
#     writer = PdfWriter()
#     with open(NEW_FOLDER / f"page{i}.pdf", "wb") as archive:
#         writer.add_page(page)
#         writer.write(archive)

files = [
    NEW_FOLDER / "page6.pdf",
    NEW_FOLDER / "page0.pdf",
    NEW_FOLDER / "page5.pdf",
    NEW_FOLDER / "page3.pdf",
    NEW_FOLDER / "page2.pdf",
    NEW_FOLDER / "page4.pdf",
    NEW_FOLDER / "page1.pdf",
    NEW_FOLDER / "page7.pdf",
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(PDF_FOLDER / "MERGED.pdf")
