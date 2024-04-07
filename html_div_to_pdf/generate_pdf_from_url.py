import os
import asyncio
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.goto(url)
    
    await page.pdf({'path': pdf_path, 'format': 'A4', 'scale': 0.76, 'left': '15cm'})
    
    await browser.close()

save_path = os.path.expanduser("~/Documents/result_aqualab_kg2.pdf")

# Run the function
asyncio.get_event_loop().run_until_complete(generate_pdf('file:///home/eddy-di/Downloads/result.aqualab.kg.html', pdf_path=save_path))