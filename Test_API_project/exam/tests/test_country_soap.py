from exam.data.countries_data import CODE, NAME, CURRENCY, CURRENCY_CODE

def test_GetCountryByCountryCode(app):
    country = app.soap.get_country_by_country_code(CODE)
    assert (country == NAME), 'Country name not found used country code'

def test_GetCurrencyByCountry(app):
    currency_country = app.soap.get_currency_country_by_country(NAME)
    assert (currency_country == CURRENCY), 'Country currency not found used country name'

def test_GetCountryByCurrencyCode(app):
    currency_code_country = app.soap.get_currency_code_by_currency_name(CURRENCY)
    country_from_currency_code = app.soap.get_country_by_currency_code(currency_code_country)
    assert (country_from_currency_code == NAME), 'Country name not found used currency code'

def test_exist_current_code_in_GetCurrencyCodeByCurrencyName_response(app):
    currency_code_list = app.soap.get_currency_code_list(CURRENCY)
    print currency_code_list
    assert (CURRENCY_CODE in currency_code_list), 'Currency code not found in list got by GetCurrencyCodeByCurrencyName method'