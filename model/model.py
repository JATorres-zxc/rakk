import pandas as pd

df = pd.read_csv("pdf_downloader\data\daily_price_1\daily_price_1_cleaned.csv", skiprows=[0], names=["Market", "Well-milledRice (Local)", "Tilapia", "Galunggong (Local)", "Egg(Medium)"])

main_df = pd.DataFrame()

# print(df.head())