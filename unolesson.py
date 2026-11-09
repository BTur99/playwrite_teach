# ФИО: Алтухов Глеб Евгеньевич
# Дата: 09-11-2026
# Время: 11:02
# Описание: установка библиотеки
"""
чтобы установить
1. uv add pytest-playwright | библиотека
2. uv run playwright install | браузеры
"""

# ФИО: Алтухов Глеб Евгеньевич
# Дата: 09-11-2026
# Время: 11:17
# Описание: запуск кода из модуля Getting started - Library(First script) 
#           открывает браузер хромиум(также можно лису или вебкит)
#           переходит на ссылку и переписывает загаловок этой страницы

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title()) 
    browser.close()

# Вывод: Fast and reliable end-to-end testing for modern web apps | Playwright