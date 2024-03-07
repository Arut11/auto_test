import time
from typing import KeysView
import path
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


                                    #Подписание назначения в ТАП
def test_select_button():
    #Перехожу по ссылке в ТАП
    path.browser.get(path.url_TAP)
    path.browser.implicitly_wait(20)

    #Кликаю кнопку "Добавить" в блоке "Назначения"
    button = WebDriverWait(path.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, path.button_add))
    )
    button.click()

    # Добавляю задержку в 2 секунды
    time.sleep(4)

    #Кликаю по полю "Препарат"
    text_field = WebDriverWait(path.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, path.drug_field))
    )
    text_field.click()

    # Ввожу в поле название препарата
    text_field.send_keys('Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(4)

    # Выбираю и кликаю по первому элементу выпадающего списка
    dropdown_list = WebDriverWait(path.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, path.element_located_1))
    )
    dropdown_list.click() 
    time.sleep(4)

    #Кликаю кнопку "Подписать"
    button_signature = WebDriverWait(path.browser, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, path.button_signature_path))
        )
    button_signature.click()
    time.sleep(20)
