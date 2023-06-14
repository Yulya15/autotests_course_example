# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
browser = webdriver.Chrome()
try:
    # Переход на сайт https://sbis.ru
    browser.get(sbis_site)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    sleep(1)

    # Переход в раздел "Контакты"
    contacts = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    assert contacts.text == 'Контакты', 'Неверный текст элемента "Контакты"'
    assert contacts.is_displayed(), 'Элемент "Контакты" не отображается'
    contacts.click()
    sleep(2)

    # Поиск баннера Тензор и переход по нему на сайт https://tensor.ru
    banner_tensor = browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor[href="https://tensor.ru/"]')
    assert banner_tensor.is_displayed(), 'Баннер "Тензор" не отображается'
    banner_tensor.click()
    sleep(5)
    browser.switch_to.window(browser.window_handles[1])
    sleep(2)
    assert browser.current_url == tensor_site, 'Неверная ссылка на сайта Тензора'

    # Проверка наличия блока "Сила в людях"
    power_people = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert power_people.is_displayed(), 'Блок "Сила в людях" не отображается'
    power_people.location_once_scrolled_into_view
    sleep(2)

    # Переход в "Подробнее" и проверка, что открывается https://tensor.ru/about
    details = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    assert details.is_displayed(), 'Элемент "Подробнее" в блоке "Сила в людях" не отображается'
    details.click()
    assert browser.current_url == 'https://tensor.ru/about', 'Неверная ссылка на сайт https://tensor.ru/about'
    sleep(2)

finally:
    browser.quit()
