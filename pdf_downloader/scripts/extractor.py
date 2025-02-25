import pdfplumber
import pandas as pd
import os

# Path to the specific PDF
pdf_path = "pdf_downloader\data\Daily_Price_2.pdf"
output_folder = pdf_path.replace(".pdf", "")

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

def extract_tables_from_pdf():
    """Extracts and cleans tables from the PDF for better accuracy."""

    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found: {pdf_path}")
        return

    os.makedirs(output_folder, exist_ok=True)

    all_data = []  # List to store all tables

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(min(3, len(pdf.pages))):  # Extract first 3 pages safely
            page = pdf.pages[page_num]
            
            # Extract table with better accuracy
            table = page.extract_table({"snap_tolerance": 3})

            if table:
                df = pd.DataFrame(table)

                # Remove completely empty rows
                df = df.dropna(how='all')

                # Ensure first row is properly assigned as headers
                df.columns = df.iloc[0].fillna("")  # Replace None values with empty strings
                df = df[1:].reset_index(drop=True)  # Remove first row and reset index

                # Ensure unique column names
                df.columns = make_column_names_unique(df.columns)

                # Fix any misaligned rows (like "NOT AVAILABLE" values)
                df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

                # Standardize column names (fix \r\n and empty names)
                df.columns = [str(col).replace("\r\n", " ").strip() for col in df.columns]

                # Fix inconsistent number ranges (e.g., "150.00 - 160.00")
                def clean_number_ranges(val):
                    if isinstance(val, str):
                        return val.replace(" ", "").replace("–", "-")
                    return val

                df = df.map(clean_number_ranges)

                # Store data for final processing
                all_data.append(df)

                # Save CSV for each page
                csv_filename = os.path.join(output_folder, f"daily_price_2_{page_num + 1}.csv")
                df.to_csv(csv_filename, index=False)
                print(f"✅ Page {page_num + 1} extracted and saved: '{csv_filename}'")
            else:
                print(f"⚠️ No valid table data found on Page {page_num + 1}.")

    # # Combine all extracted tables into one CSV
    # if all_data:
    #     try:
    #         final_df = pd.concat(all_data, ignore_index=True)
    #         final_csv_path = os.path.join(output_folder, "daily_price_combined.csv")
    #         final_df.to_csv(final_csv_path, index=False)
    #         print(f"🚀 Final cleaned data saved to '{final_csv_path}'")
    #     except Exception as e:
    #         print(f"❌ Error combining tables: {e}")

if __name__ == "__main__":
    extract_tables_from_pdf()
