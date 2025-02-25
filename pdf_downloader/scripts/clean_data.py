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

# ✅ Convert Market names to numeric codes
market_codes = {}
base_number = 0  # Set to 0 so first becomes 1.1
sub_number = 0.0  # Sub number starts at 0.1

for market in df["Market"]:
    if market in market_codes:
        continue  # If already assigned, skip

    if "/" in market:
        base_number += 1  # Increment base when '/' is found
        sub_number = 0.0  # Reset sub number

    sub_number += 0.1  # Always increase decimal part
    market_codes[market] = round(base_number + sub_number, 1)

df["Market"] = df["Market"].map(market_codes)  # Replace market names

# ✅ Function to clean and get average of price values
def clean_price(value):
    """Convert price range to average, replace 'NOT AVAILABLE' or empty with -1.0."""
    if isinstance(value, str):
        if "NOT AVAILABLE" in value or value.strip() == "":
            return -1.0
        
        numbers = re.findall(r"\d+\.\d+|\d+", value)  # Extract numeric values
        numbers = list(map(float, numbers)) 
        
        if len(numbers) == 2:
            return round(sum(numbers) / 2, 2)  # Average of range
        elif len(numbers) == 1:
            return round(numbers[0], 2)

    return -1.0  # Default for NaN or invalid values

# ✅ Apply function to all numeric columns except "Market"
numeric_columns = df.columns[1:]
df[numeric_columns] = df[numeric_columns].map(clean_price)

# ✅ Convert all values to float and round to 2 decimal places
df = df.astype(float).applymap(lambda x: round(x, 2))

# ✅ Save Cleaned Data
clean_csv_path = "pdf_downloader/data/daily_price_1/daily_price_3_cleaned.csv" 
df.to_csv(clean_csv_path, index=False, float_format="%.2f")  # Ensure 2 decimal places in output

print(f"✅ Cleaned data saved at: {clean_csv_path}")
print(df.dtypes)  # Display data types to confirm everything is float
print(df.head())  # Display cleaned data
