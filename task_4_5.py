from urllib.request import urlopen
import xml.etree.ElementTree as ET
from datetime import datetime
import sys


def currency_rates(currency):

    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:

        root = ET.parse(r).getroot()

        # get date
        date = root.attrib['Date']

        # str to datetime
        ###################################################
        ########### TASK 3 ################################
        datetime_object = datetime.strptime(date, '%d.%m.%Y')
        print('Date is %s: ' % datetime_object)
        print('type of the data %s: ' % type(datetime_object))

        ###################################################
        ########## TASK 2 #################################
        ruble = None
        for valute in root:

            for attrs in valute:
                if attrs.text == currency.upper():


                    ruble = float(valute[4].text.replace(',', '.'))

                    break


        return ruble, datetime_object



kurs, date = currency_rates(sys.argv[1])
print(kurs, date)