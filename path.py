
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

    #Ссылка на ТАП
url_TAP = 'http://192.168.7.218/test/statist/purpose/3648973/523452F6-124E-4D63-94C4-012D71072FD3/2023-01-17T00:00:00/jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D?ticket=jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D&DocPrvdId=2000&MisUrl=https:%2F%2Ftest.2dr.ru%2Fdemo&ReturnUrl=http:%2F%2Ftest.2dr.ru%2Fdemo%2FTap'

    #Кнопка "Добавить" блока назначения в ТАП
button_add = '#appointment > app-appointment > div > div.row.mb-0.appointment__datatable > div > div > app-st-table > div > div:nth-child(4)'

    #Поле "Препарат" формы назначения в ТАП
drug_field = '#appointmentAdding > appointment-add > div.appointment-add.ng-tns-c236-9 > div > div > mat-card > form > div:nth-child(3) > div > div:nth-child(1) > st-autocomplete > mat-form-field input'

    #Первый элемент выпадающего списка в поле "Препарат" формы назначения в ТАП
element_located_1 = '.mat-option-text'

    #Кнопка "Подписать" формы назначения в ТАП
button_signature_path = '#appointmentAdding > appointment-add > div.appointment-add.ng-tns-c236-9 > div > div > mat-card > div.appointment-btns-block > div > div:nth-child(3)'