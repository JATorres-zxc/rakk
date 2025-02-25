import pandas as pd
import numpy as np
import re

# Load the CSV File
csv_path = "pdf_downloader/data/daily_price_1/daily_price_1_3.csv"  # Change if needed
df = pd.read_csv(csv_path, skiprows=[0], header=[0])

# ✅ Ensure all column names are strings
df.columns = df.columns.astype(str)

# ✅ Remove Unnamed Columns
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

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

# ✅ Ensure "Tomato" and "Cabbage" are next to each other
if "Tomato" in df.columns and "Cabbage" in df.columns:
    columns = list(df.columns)
    columns.remove("Cabbage")  # Remove Cabbage
    tomato_idx = columns.index("Tomato")  # Find Tomato index
    columns.insert(tomato_idx + 1, "Cabbage")  # Insert Cabbage after Tomato
    df = df[columns]  # Reorder dataframe columns

# ✅ Save Cleaned Data
clean_csv_path = "pdf_downloader/data/daily_price_1/daily_price_3_cleaned.csv"
df.to_csv(clean_csv_path, index=False)

print(f"✅ Cleaned data saved at: {clean_csv_path}")
print(df.head())  # Display cleaned data
