from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Zhuge_Liang")
    page.locator('xpath=//*[@id="searchInput"]').click()
    page.fill('//*[@id="searchInput"]', 'Three Kingdoms')
    page.locator('xpath=/html/body/div[5]/div/a[1]').click()
    page.locator('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/th/a').click()
    page.locator( '// *[ @ id = "mw-content-text"] / div[1] / table[2] / tbody / tr[2] / td / a / img').click()
    page.locator('xpath=/ html / body / div[6] / div / div[1] / a[1]').click()
    page.locator('xpath=/html/body/div[6]/div/div[2]/div/div[3]/div[3]/div[1]/a[1]/span[1]').click()
    time.sleep(5)



