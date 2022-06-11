from urllib.request import urlopen
import xml.etree.ElementTree as ET
from datetime import datetime


def currency_rates(currency):

    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:

        root = ET.parse(r).getroot()


        ###################################################
        ########## TASK 2 #################################
        ruble = None
        for valute in root:

            for attrs in valute:
                if attrs.text == currency.upper():


                    ruble = float(valute[4].text.replace(',', '.'))

                    break


        return ruble




x = currency_rates('UsD')
