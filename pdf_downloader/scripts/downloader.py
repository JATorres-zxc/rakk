import os
import time
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
os.makedirs("data", exist_ok=True)

# Set up Selenium WebDriver
options = Options()
options.headless = False  # Change to False to see the browser (for debugging)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_pdf_links():
    """Extracts the first 3 PDF links from the 'Daily Retail Price Range' table."""
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

        # Get the first 3 links only
        pdf_links = [link.get_attribute("href") for link in date_links[:3] if link.get_attribute("href").endswith(".pdf")]

        return pdf_links

    except Exception as e:
        print(f"❌ Error finding PDFs: {e}")
        return []

def download_pdfs(pdf_links):
    """Downloads the selected PDFs and saves them locally."""
    for index, pdf_url in enumerate(pdf_links):
        pdf_filename = f"pdf_downloader/data/Daily_Price_{index + 1}.pdf"
        response = requests.get(pdf_url)

        if response.status_code == 200:
            with open(pdf_filename, "wb") as file:
                file.write(response.content)
            print(f"✅ Downloaded: {pdf_filename}")
        else:
            print(f"❌ Failed to download {pdf_url}")

if __name__ == "__main__":
    print("🔍 Extracting PDF links from 'Daily Retail Price Range' table...")
    pdf_links = get_pdf_links()
    
    if pdf_links:
        print(f"✅ Found {len(pdf_links)} PDFs! Downloading the first 3...")
        download_pdfs(pdf_links)
    else:
        print("❌ No PDFs found in the 'Daily Retail Price Range' table.")
    
    driver.quit()
