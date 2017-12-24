# -*- coding: utf-8 -*-

class SoapHelper:
    def __init__(self,app):
        self.app = app

    def get_country_by_country_code(self, code):
        client = self.app.client
        # вызываем метод и получаем xml спользуя библиотеку suds
        data_xml = client.service.GetCountryByCountryCode(code)
        # выполняем парсинг xml с помошью библиотеки lxml
        return self.app.lxml.get_name_from_xml(data_xml)

    def get_currency_country_by_country(self, name_country):
        client = self.app.client
        data_xml = client.service.GetCurrencyByCountry(name_country)
        return self.app.lxml.get_currency_from_xml(data_xml)

    def get_currency_code_by_currency_name(self, currency_country):
        client = self.app.client
        data_xml = client.service.GetCurrencyCodeByCurrencyName(currency_country)
        return self.app.lxml.get_currency_code_from_xml(data_xml)

    def get_country_by_currency_code(self, currency_code_country):
        client = self.app.client
        data_xml = client.service.GetCountryByCurrencyCode(currency_code_country)
        return self.app.lxml.get_country_from_currency_code_from_xml(data_xml)

    def get_currency_code_list(self, currency_country):
        client = self.app.client
        data_xml = client.service.GetCurrencyCodeByCurrencyName(currency_country)
        return self.app.lxml.get_currency_code_list_from_xml(data_xml)