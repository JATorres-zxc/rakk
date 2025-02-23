import pdfplumber
import pandas as pd
import os

# Path to the specific PDF for testing
pdf_path = "pdf_downloader/data/daily_price_1.pdf"
output_folder = pdf_path.replace(".pdf", "")  # Folder: daily_price_1/

def extract_tables_from_pdf():
    """Extracts tables from pages 1 to 3 of `daily_price_1.pdf`, saves each page separately."""

    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found: {pdf_path}")
        return

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(0, 3):  # Pages 1 to 3 (Python index starts at 0)
            if page_num < len(pdf.pages):
                page = pdf.pages[page_num]
                table = page.extract_table()

                if table:
                    structured_data = [row for row in table]

                    # Convert to DataFrame
                    df = pd.DataFrame(structured_data)

                    # Remove empty rows
                    df = df.dropna(how='all')

                    if not df.empty:
                        # Save each page as a separate CSV file
                        csv_filename = os.path.join(output_folder, f"daily_price_1_{page_num + 1}.csv")
                        df.to_csv(csv_filename, index=False)
                        print(f"✅ Page {page_num + 1} extracted and saved: '{csv_filename}'")
                    else:
                        print(f"⚠️ No valid table data found on Page {page_num + 1}.")

if __name__ == "__main__":
    extract_tables_from_pdf()
