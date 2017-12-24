# coding=utf-8

from lxml import etree

class ParsingXml():
    def __init__(self):
        pass

    @staticmethod
    def get_name_from_xml(body_xml):
        root = etree.XML(body_xml)
        find = etree.XPath("//name/text()")
        value = find(root)[0]
        return value

    @staticmethod
    def get_currency_from_xml(body_xml):
        root = etree.XML(body_xml)
        find = etree.XPath("//Currency/text()")
        value = find(root)[0]
        return value

    @staticmethod
    def get_currency_code_from_xml(body_xml):
        root = etree.XML(body_xml)
        find = etree.XPath("//CurrencyCode/text()")
        value = find(root)[2]
        return value

    @staticmethod
    def get_country_from_currency_code_from_xml(body_xml):
        root = etree.XML(body_xml)
        find = etree.XPath("//Name/text()")
        value = find(root)[0]
        return value

    @staticmethod
    def get_currency_code_list_from_xml(body_xml):
        root = etree.XML(body_xml)
        find = etree.XPath("//CurrencyCode/text()")
        value = find(root)
        return value