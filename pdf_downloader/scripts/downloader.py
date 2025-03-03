import os
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Website URL
WEBSITE_URL = "https://www.da.gov.ph/price-monitoring/"

# Folder to save PDFs
SAVE_FOLDER = "data"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Set up Selenium WebDriver
options = Options()
options.headless = False  # Set to True for headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def format_date(date_text):
    """Formats the date to be used as a filename (e.g., 'February 25, 2025' -> 'February_25_2025')."""
    return date_text.replace(",", "").replace(" ", "_")

def get_pdf_links():
    """Extracts PDF links and corresponding dates from the 'Daily Retail Price Range' table (2022-2025)."""
    driver.get(WEBSITE_URL)

    # Wait for JavaScript content to load
    time.sleep(5)

    try:
        # Locate the table by its ID
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "tablepress-65"))
        )
        print("✅ Found the 'Daily Retail Price Range' table!")

        # Find all links inside the table
        date_links = table.find_elements(By.XPATH, ".//a")

        pdf_data = []
        for link in date_links:
            href = link.get_attribute("href")
            date_text = link.text  # Get the text (date)

            # Filter only PDFs from 2022-2025
            if href and href.endswith(".pdf") and any(year in date_text for year in ["2022", "2023", "2024", "2025"]):
                formatted_date = format_date(date_text)
                pdf_data.append((href, formatted_date))

        return pdf_data

    except Exception as e:
        print(f"❌ Error finding PDFs: {e}")
        return []

def download_pdf(pdf_url, pdf_filename, max_retries=5):
    """Downloads a single PDF with retries and exponential backoff."""
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(pdf_url, timeout=10)  # Timeout after 10 sec
            
            if response.status_code == 200:
                with open(pdf_filename, "wb") as file:
                    file.write(response.content)
                print(f"✅ Downloaded: {pdf_filename}")
                return True
            else:
                print(f"⚠️ Failed to download {pdf_url} (Status Code: {response.status_code})")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error downloading {pdf_url}: {e}")

        # Wait before retrying (exponential backoff)
        wait_time = 2 ** attempt + random.uniform(0, 1)
        print(f"⏳ Retrying in {round(wait_time, 2)} seconds...")
        time.sleep(wait_time)
        attempt += 1

    print(f"❌ Giving up on {pdf_url} after {max_retries} attempts.")
    return False

def download_pdfs(pdf_data):
    """Downloads all matched PDFs with retries and rate limiting."""
    for pdf_url, formatted_date in pdf_data:
        pdf_filename = os.path.join(SAVE_FOLDER, f"{formatted_date}.pdf")

        # Download with retry logic
        download_success = download_pdf(pdf_url, pdf_filename)

        # Throttle requests (random delay to avoid detection)
        if download_success:
            delay = random.uniform(1, 3)  # Random delay between 1-3 sec
            print(f"⏳ Waiting {round(delay, 2)} seconds before the next request...")
            time.sleep(delay)

if __name__ == "__main__":
    print("🔍 Extracting PDF links from 'Daily Retail Price Range' table (2022-2025)...")
    pdf_data = get_pdf_links()
    
    if pdf_data:
        print(f"✅ Found {len(pdf_data)} PDFs! Downloading them now...")
        download_pdfs(pdf_data)
    else:
        print("❌ No PDFs found for the years 2022-2025.")
    
    driver.quit()
