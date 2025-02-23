import scripts.downloader as downloader
import scripts.extractor as extractor

if __name__ == "__main__":
    print("🚀 Starting automated PDF downloader...\n")

    # Step 1: Scrape & Download PDFs
    pdf_links = downloader.get_pdf_links(downloader.WEBSITE_URL)
    if pdf_links:
        downloader.download_pdfs(pdf_links)

        # Step 2: Extract Text from PDFs
        extractor.extract_text_from_pdfs()
        print("\n🎉 All PDFs downloaded & processed successfully!")
    else:
        print("❌ No PDFs found.")
