from playwright.sync_api import sync_playwright
from tts import speak

def open_browser(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(
            url,
            wait_until='domcontentloaded'
            )
        
        first_paragraph_selector = 'div#mw-content-text > div.mw-parser-output > p:not(.mw-empty-elt):not(.mw-disambig):not(.hatnote):not([class^="mw-redirectedfrom"])'
        
        first_paragraph = page.locator(first_paragraph_selector).first
        
        if first_paragraph:
            text = first_paragraph.text_content().strip()
            speak(text)
        else:
            speak("First paragraph not found.")

        input("Press 'ENTER' to quit.")
        browser.close()