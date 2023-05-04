import requests

# Определение значений переменных
city = 'Москва'
vacancy = 'QA Engineer'
salary = '180000'
page = '1'
per_page = '20'
only_with_salary = 'true'
# Формирование URL для запроса за городом
areas_url = 'https://api.hh.ru/suggests/areas?text=' + city

# Отправка запроса за городом
areas_response = requests.get(areas_url)

# Обработка ответа по городу
areas_json_response = areas_response.json()

# Извлечение значения id из ответа
area_id = None

if 'items' in areas_json_response and len(areas_json_response['items']) > 0:
    area_id = areas_json_response['items'][0]['id']

# Формирование URL для запроса за квериками поиска
dictionaries_url = 'https://api.hh.ru/dictionaries'

# Отправка запроса за квери
dictionaries_response = requests.get(dictionaries_url)

# Обработка ответа с квери
dictionaries_json_response = dictionaries_response.json()

# Извлечение значения id из массива "experience"
experience_array = dictionaries_json_response.get('experience', [])
experience_id = None

for experience_object in experience_array:
    if experience_object.get('name') == 'От 3 до 6 лет':
        experience_id = experience_object.get('id')
        break

# Извлечение значения id из массива "employment"
employment_array = dictionaries_json_response.get('employment', [])
employment_id = None

for employment_object in employment_array:
    if employment_object.get('name') == 'Полная занятость':
        employment_id = employment_object.get('id')
        break

# Вывод значений переменных
print('Area ID:', area_id)
print('Experience ID:', experience_id)
print('Employment ID:', employment_id)

# Формирование URL для запроса за вакансиями
vacancies_url = 'https://api.hh.ru/vacancies?page=' + page + '&per_page=' + per_page + '&text=' + vacancy + '&experience=' + experience_id + '&area=' + area_id + '&salary=' + salary + '&only_with_salary=' + only_with_salary + '&employment=' + employment_id

# Отправка запроса за вакансиями
vacancies_response = requests.get(vacancies_url)

#Обработка ответа вакансий

vacancies_json_response = vacancies_response.json()

print('response:', vacancies_json_response)