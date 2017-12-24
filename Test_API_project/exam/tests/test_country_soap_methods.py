# -*- coding: utf-8 -*-
from exam.data.countries_data import CODE, NAME, CURRENCY, CURRENCY_CODE

'''
Это первый вариант тестов исходящий из условия что все проверки выполняются внутри одного теста так как они связаны
между собой и используют результаты друг друга
'''

def test_country_soap_methods(app):

    # проверка метода GetCountryByCountryCode
    country = app.soap.get_country_by_country_code(CODE)
    assert(country == NAME), 'Country name not found used country code'

    # проверка метода GetCurrencyByCountry
    currency_country = app.soap.get_currency_country_by_country(country)
    assert(currency_country == CURRENCY), 'Country currency not found used country name'

    # проверка метода GetCountryByCurrencyCode
    currency_code_country = app.soap.get_currency_code_by_currency_name(currency_country)
    country_from_currency_code = app.soap.get_country_by_currency_code(currency_code_country)
    assert (country_from_currency_code == NAME), 'Country name not found used currency code'

    # проверка присутствия полученного кода валюты в списке кодов метода GetCurrencyCodeByCurrencyName
    currency_code_list = app.soap.get_currency_code_list(currency_country)
    print currency_code_list
    assert (CURRENCY_CODE in currency_code_list)

