# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

fix_site = 'https://fix-online.sbis.ru/'
autorization_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
msg = 'О, привет!'
browser = webdriver.Chrome()
try:
    # Авторизация на сайте https://fix-online.sbis.ru/
    browser.get(fix_site)
    assert browser.current_url == autorization_site, 'Неверно открыт сайт'
    sleep(1)
    user_login, user_password = 'Ясникова', 'Ясникова123'
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    assert login.is_displayed(), 'Поле для ввода логина не отображается'
    login.clear()
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(2)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)
    assert browser.current_url == fix_site, 'Не перешли на сайт https://fix-online.sbis.ru/'

    # Переход в раздел Контакты
    accordion_contacts = browser.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert accordion_contacts.is_displayed(), 'Пункт "Контакты" в аккордеоне не отображается'
    accordion_contacts.click()
    sleep(2)
    submenu_contacts = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
    assert submenu_contacts.is_displayed(), 'Пункт "Контакты" в подменю не отображается'
    submenu_contacts.click()
    sleep(2)

    # Создание сообщения самому себе
    add_btn = browser.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert add_btn.is_displayed(), "Кнопка для создания сообщения не отображается"
    add_btn.click()
    sleep(2)
    addressee_window = browser.find_element(By.CSS_SELECTOR, '.controls-Popup.ws-float-area-show-complete')
    assert addressee_window.is_displayed(), "Окно добавления адресата не открылось"
    search = browser.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field[name="ws-input_2023-06-13"]')
    assert search.is_displayed(), "Поисковая строка не отображается"
    search.send_keys('Ясникова', Keys.ENTER)
    sleep(2)
    search.send_keys(Keys.ENTER)
    sleep(2)
    message = browser.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    assert message.is_displayed(), "Поле для ввода сообщения не найдено"
    message.send_keys(msg)
    sleep(2)

    # Отправка сообщения и проверка отправки
    send_message = browser.find_element(By.CSS_SELECTOR, '.controls-Button__icon.icon-BtArrow')
    assert send_message.is_displayed(), "Нет кнопки отправки сообщения"
    send_message.click()
    sleep(2)
    find_message = browser.find_element(By.XPATH, ".//p[contains(text(), msg)]")
    assert find_message.is_displayed(), "Отправленное сообщение отсутствует"

    # Удаление сообщения и проверка удаления
    action_chains = ActionChains(browser)
    action_chains.move_to_element(find_message)
    action_chains.perform()
    sleep(2)
    delete_message = browser.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_message.click()
    sleep(2)
    assert browser.find_elements(By.XPATH, ".//p[contains(text(), msg)]")[0] != msg, 'Сообщение не удалено!'
    sleep(2)

finally:
    browser.quit()

