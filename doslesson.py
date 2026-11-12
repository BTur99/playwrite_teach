# ФИО: Алтухов Глеб Евгеньевич
# Дата: 10-11-2026
# Время: 11:26
# Описание: запуск кода из модуля Getting started - Library(Interactive mode (REPL)) 
#           открывает браузер хромиум
#           переходит на ссылку и делает скрин и сохраняет скрин в example.png

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()

# Резултат: скрин example.png