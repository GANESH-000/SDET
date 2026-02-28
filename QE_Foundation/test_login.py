from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        file_path = "file://" + os.path.abspath("./QE_Foundation/index.html")
        page.goto(file_path)

        page.fill("#username", "admin")
        page.fill("#password", "1234")
        page.click("#loginBtn")

        page.wait_for_timeout(3000)
        browser.close()

run()