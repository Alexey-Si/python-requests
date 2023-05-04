import requests
import pytest

# Переменные
city = 'Москва'
vacancy = 'QA Engineer'
salary = '180000'
page = '1'
per_page = '20'
only_with_salary = 'true'

def test_areas_request():
    areas_url = 'https://api.hh.ru/suggests/areas?text=' + city

    response = requests.get(areas_url)
    areas_json_response = response.json()

    # Проверяем статус код
    assert response.status_code == 200

    # Проверяем наличие объектов "items", "id", "text", "url" в теле ответа
    assert 'items' in areas_json_response
    assert 'id' in areas_json_response['items'][0]
    assert 'text' in areas_json_response['items'][0]
    assert 'url' in areas_json_response['items'][0]

def test_dictionaries_request():
    dictionaries_url = 'https://api.hh.ru/dictionaries'

    response = requests.get(dictionaries_url)
    dictionaries_json_response = response.json()

    # Проверяем статус код
    assert response.status_code == 200

    # Проверяем наличие объектов "experience" и "employment" в теле ответа
    assert 'experience' in dictionaries_json_response
    assert 'employment' in dictionaries_json_response

def test_vacancies_request():
    areas_url = 'https://api.hh.ru/suggests/areas?text=' + city
    areas_response = requests.get(areas_url)
    areas_json_response = areas_response.json()

    area_id = None
    if 'items' in areas_json_response and len(areas_json_response['items']) > 0:
        area_id = areas_json_response['items'][0]['id']

    dictionaries_url = 'https://api.hh.ru/dictionaries'
    dictionaries_response = requests.get(dictionaries_url)
    dictionaries_json_response = dictionaries_response.json()

    experience_id = None
    for experience_object in dictionaries_json_response.get('experience', []):
        if experience_object.get('name') == 'От 3 до 6 лет':
            experience_id = experience_object.get('id')
            break

    employment_id = None
    for employment_object in dictionaries_json_response.get('employment', []):
        if employment_object.get('name') == 'Полная занятость':
            employment_id = employment_object.get('id')
            break

    vacancies_url = 'https://api.hh.ru/vacancies?page=' + page + '&per_page=' + per_page + '&text=' + vacancy + '&experience=' + experience_id + '&area=' + area_id + '&salary=' + salary + '&only_with_salary=' + only_with_salary
    response = requests.get(vacancies_url)
    vacancies_json_response = response.json()
    
    # Проверяем статус код
    assert response.status_code == 200

    # Проверяем наличие объектов "items", "found", "pages", "per_page", "page", "clusters", "arguments", "alternate_url" в теле ответа
    assert 'items' in vacancies_json_response
    assert 'found' in vacancies_json_response
    assert 'pages' in vacancies_json_response
    assert 'per_page' in vacancies_json_response
    assert 'page' in vacancies_json_response
    assert 'clusters' in vacancies_json_response
    assert 'arguments' in vacancies_json_response
    