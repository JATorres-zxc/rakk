import pandas as pd
import numpy as np
import re

# Load the CSV File
csv_path = "pdf_downloader/data/daily_price_1/daily_price_1_2.csv"  # Change if needed

# Read CSV, extract column names from the second row
df = pd.read_csv(csv_path, skiprows=[0])  # Skip first row (index numbers)
df.columns = df.iloc[0]  # Set column names from second row
df = df[1:].reset_index(drop=True)  # Remove the original row used for headers

# ✅ Ensure all column names are strings (Fix TypeError)
df.columns = df.columns.astype(str)

# ✅ Ensure "Market" column is properly named
df.rename(columns={df.columns[0]: "Market"}, inplace=True)

# ✅ Clean column names (fixing newlines and unnecessary characters)
df.columns = [re.sub(r'\s+', ' ', col).strip().replace("\n", " ") for col in df.columns]
df.columns = [col.replace("*", "").replace("  ", " ") for col in df.columns]  # Remove '*' & double spaces

# ✅ Keep original price ranges, replace "NOT AVAILABLE" with "None"
def clean_price(value):
    """Ensure price ranges remain as strings and replace 'NOT AVAILABLE' with 'None'."""
    if isinstance(value, str):
        if "NOT AVAILABLE" in value:
            return "None"  # Explicitly mark unavailable data
        numbers = re.findall(r"\d+\.\d+|\d+", value)  # Extract numbers
        if len(numbers) == 2:
            return f"{numbers[0]}-{numbers[1]}"  # Keep full range
        elif len(numbers) == 1:
            return numbers[0]  # Keep single price
    return "None"  # Default to None if empty or invalid

# ✅ Apply function to all numeric columns except "Market"
numeric_columns = df.columns[1:]  # Exclude "Market"
for col in numeric_columns:
    df[col] = df[col].apply(clean_price)

# ✅ Save Cleaned Data
clean_csv_path = "pdf_downloader/data/daily_price_1/daily_price_2_cleaned.csv"
df.to_csv(clean_csv_path, index=False)

print(f"✅ Cleaned data saved at: {clean_csv_path}")
print(df.head())  # Display cleaned data
