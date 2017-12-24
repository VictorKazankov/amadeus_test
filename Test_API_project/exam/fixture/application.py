# -*- coding: utf-8 -*-
from suds.client import Client
from exam.fixture.soap import SoapHelper
from exam.utils.parsing_xml_library import ParsingXmlLibrary

class Application:
   def __init__(self):
        self.client = Client("http://www.webservicex.net/country.asmx?WSDL")
        self.soap = SoapHelper(self)
        self.lxml = ParsingXmlLibrary()
