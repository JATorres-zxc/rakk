import os
import pandas as pd

# Folder containing extracted CSV files
csv_folder = "data/extracted_data"

def clean_csv_files():
    """Removes columns where the first row (index 0) is NaN from all CSV files."""
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

    if not csv_files:
        print("❌ No CSV files found in 'data/extracted_data'. Exiting process.")
        return

    for csv_filename in csv_files:
        csv_path = os.path.join(csv_folder, csv_filename)

        try:
            # Load CSV
            df = pd.read_csv(csv_path)

            # Find columns where the first row (index 0) is NaN
            nan_columns = df.columns[df.iloc[0].isna()].tolist()

            if nan_columns:
                # Drop the identified columns
                df_cleaned = df.drop(columns=nan_columns)
                
                # Overwrite the CSV file with cleaned data
                df_cleaned.to_csv(csv_path, index=False)
                
                print(f"✅ Cleaned '{csv_filename}', removed columns: {nan_columns}")
            else:
                print(f"✔️ No columns to remove in '{csv_filename}', skipping.")

        except Exception as e:
            print(f"❌ Error processing '{csv_filename}': {e}")

if __name__ == "__main__":
    clean_csv_files()
