import os
import pdfplumber
import pandas as pd
import re

# Folder containing PDFs
pdf_folder = "data"
output_folder = os.path.join(pdf_folder, "extracted_data")
os.makedirs(output_folder, exist_ok=True)

# Store issues for summary
extraction_summary = []

def log_issue(issue):
    """Logs issues to the summary list."""
    print(issue)  # Print immediately
    extraction_summary.append(issue)  # Store for later

def make_column_names_unique(columns):
    """Ensure unique column names by appending numbers to duplicates."""
    seen = {}
    unique_columns = []
    for col in columns:
        if col in seen:
            seen[col] += 1
            unique_columns.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            unique_columns.append(col)
    return unique_columns

def extract_date_from_filename(pdf_filename):
    """Extracts the date from the PDF filename."""
    match = re.search(r"([A-Za-z]+)_(\d{1,2})_(\d{4})", pdf_filename)
    if match:
        month, day, year = match.groups()
        return f"{month} {day}, {year}"  # Format as "April 1, 2022"
    return None  # Return None if no date found

def extract_tables_from_pdf(pdf_path, extracted_date):
    """Extracts tables from Page 2 of the PDF."""
    
    with pdfplumber.open(pdf_path) as pdf:
        if len(pdf.pages) < 2:
            log_issue(f"❌ {pdf_path}: No Page 2 found. Skipping.")
            return None
        
        page = pdf.pages[1]  # Page 2 (zero-indexed)

        # Extract table
        table = page.extract_table({"snap_tolerance": 6})
        if not table:
            log_issue(f"⚠️ {pdf_path}: No valid table detected on Page 2.")
            return None
        
        df = pd.DataFrame(table)
        df = df.dropna(how='all')  # Remove empty rows

        # Set the first row as header
        df.columns = df.iloc[0].fillna("")
        df = df[1:].reset_index(drop=True)

        # Ensure unique column names
        df.columns = make_column_names_unique(df.columns)

        # Standardize column names
        df.columns = [str(col).replace("\r\n", " ").strip() for col in df.columns]

        # Strip unnecessary spaces in data
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        # Insert 'Date' column
        df.insert(0, "Date", extracted_date)

        return df

def process_pdfs():
    """Processes all PDFs in the 'data' folder, extracting tables and saving as CSV."""
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    if not pdf_files:
        print("❌ No PDFs found in the 'data' folder. Exiting process.")
        return

    for pdf_filename in sorted(pdf_files):  # Process in order
        pdf_path = os.path.join(pdf_folder, pdf_filename)

        # Extract date from filename
        extracted_date = extract_date_from_filename(pdf_filename)
        if not extracted_date:
            log_issue(f"❌ {pdf_filename}: Could not extract date from filename. Skipping.")
            continue

        extracted_data = extract_tables_from_pdf(pdf_path, extracted_date)

        if extracted_data is not None:
            # Save CSV with date in filename
            formatted_date = extracted_date.replace(",", "").replace(" ", "_")  # Format for filename
            csv_filename = os.path.join(output_folder, f"daily_price_{formatted_date}.csv")
            extracted_data.to_csv(csv_filename, index=False)
            print(f"✅ Extracted data saved to '{csv_filename}'")
        else:
            log_issue(f"⚠️ {pdf_filename}: No data extracted.")

    # Save summary report with UTF-8 encoding
    summary_path = os.path.join(output_folder, "extraction_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(extraction_summary))

    print("\n📌 Extraction Summary Report:")
    print("\n".join(extraction_summary))
    print(f"\n📄 Summary saved to: {summary_path}")

if __name__ == "__main__":
    process_pdfs()
