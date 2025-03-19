from playwright.sync_api import sync_playwright
import os

login = "Jarmil"
password = "Admin123"


def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill('input[id="login"]', login)
        page.fill('input[id="pass"]', password)

        page.click('button[class="login-btn"]')
        zprava = page.locator('div[class="psst"]').text_content() 
        print(zprava)
        

        input("Klikni na cokoliv pro zavření prohlížeče")
        browser.close()
    

if __name__ == "__main__":
    main())
