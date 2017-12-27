# Test API

This repo contains test framework is used for testing of API methods at [www.webservicex.net](http://www.webservicex.net/country.asmx?WSDL) site

#### Test framework has 4 components:

* **fixture folder** contains application.py file to manage tests, soap.py file with SoapHelper class and parsing xml class
In fixture there is also soap.py file, which has accesses in webservice methods by suds library

* **tests folder** consists of test_country_soap.py file with tests in following sequence:
    * test_GetCountryByCountryCode - test for get name country from country code
	* test_GetCurrencyByCountry - test for get currency name from country name
	* test_GetCountryByCurrencyCode - test for get country name from currency code
	* test_exist_current_code_in_GetCurrencyCodeByCurrencyName_response - test for verify presence of currency code in currency's list

* **utils folder** has parsing_xml.py file which has static methods implement xml parsing with the help of lxml library

* **data folder** has countries_data.py with test data for validation of API work methods(present only Qatar country)
