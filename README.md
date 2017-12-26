# Test API project

This repo contains test framework intended for testing API methods on [www.webservicex.net](http://www.webservicex.net/country.asmx?WSDL) site

#### Test framework have 4 components:

* **fixture folder** has application.py file for rule interaction between tests, soap.py file with SoapHelper class and parsing xml class
Here also client initialized for SoapHelper class and accesses in webservice methods by suds library

* **tests folder** has test_country_soap.py file with tests in following sequence:
    * test_GetCountryByCountryCode - test for get name country from country code
	* test_GetCurrencyByCountry - test for get currency name from country name
	* test_GetCountryByCurrencyCode - test for get country name from currency code
	* test_exist_current_code_in_GetCurrencyCodeByCurrencyName_response - test for verify presence of currency code in currencies list

* **utils folder** has parsing_xml.py file consists static methods implementing xml parsing used lxml library

* **data folder** has countries_data.py with test data for validation work API methods(present only Qatar country)
