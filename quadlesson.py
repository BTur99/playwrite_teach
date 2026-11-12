# ФИО: Алтухов Глеб Евгеньевич
# Дата: 12-11-2026
# Время: 09:58
# Описание: Не протсо вводит логин а еще проверяет на тайтл на поля
# Изменения: Добавил базовый шаблон теста с примерами проверок видимости, кликабельности

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://github.com/login")
    expect(page).to_have_title("Sign in to GitHub · GitHub") # проверяет заголовок страницы
    login_input = page.get_by_role("textbox", name="Username or email address")
    login_input.fill("Your name")
    expect(login_input).to_have_value("Your name") # проверяет что текст ввелся
    sign_in_btn = page.get_by_role("button", name="Sign in")
    expect(sign_in_btn).to_be_enabled() # проверяе что кнопка активна
    sign_in_btn.click(force=True)
    page.screenshot(path="example1.png")
    browser.close()

# результат: выполняет проверки жмет кнопки 