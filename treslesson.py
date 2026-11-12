# ФИО: Алтухов Глеб Евгеньевич
# Дата: 11-11-2026
# Время: 12:42
# Описание: Этот код открывает странцу логина гит хаба и вводит туда логин|пароль а также нажимает кнопку войти
# Изменения: Поменял ссылку на логин гитхаба добавил функционал логина а потом результат сохраняет скрином
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://github.com/login")
    print(page.title())
    page.get_by_role("textbox", name="Username or email address").fill("Your name") # заполняет бокс с емаил
    page.get_by_role("textbox", name="Password").fill("Your password") # заполняет бокс с пассом
    page.get_by_role("button", name="Sign in").click() # кликает на кнопку войти
    page.screenshot(path="login.png")
    browser.close()

# Результат: пишет заголовок и делает серин проделанной работы 