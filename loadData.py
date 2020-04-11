######################### LIBRARIES #########################
import os # info about file
import sys # better management of the exceptions
from termcolor import colored # customize ui
import pandas as pd # open excel file
from datetime import datetime # managing datatime records

dataLocation ='data.xlsx'


class loadData:

    def __init__(self):
        try:
            mostRecentVersionDate = datetime.fromtimestamp(os.stat(dataLocation).st_mtime)
            print(colored("Loading data... " + str(mostRecentVersionDate), 'blue'))
        except Exception as e:
            print(colored(str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))

    def activeCases(self):
        try:
            table = pd.read_excel(dataLocation,sheet_name='activeCases') # open table
            tableColumns = table.columns.ravel()
            dates = tableColumns[1:] # create dates array
            region = table['Region'] # create region array
            return table, region, dates
        except Exception as e:
            print(colored("The following exception was catched:" + str(e), 'red'))
            print(colored("Make sure you have " + dataLocation + " in the same directory of the ICE bundle.", 'red'))

    def totalCases(self):
        try:
            table = pd.read_excel(dataLocation,sheet_name='totalCases') # open table
            tableColumns = table.columns.ravel()
            dates = tableColumns[1:] # create dates array
            datesInMillisecond = self.fromDatetimeToMillisecond(dates)
            region = table['Groups'] # create region array
            return table, region, dates, datesInMillisecond
        except Exception as e:
            print(colored("The following exception was catched:" + str(e), 'red'))
            print(colored("Make sure you have " + dataLocation + " in the same directory of the ICE bundle.", 'red'))

    def fromDatetimeToMillisecond(self, dates):
        # cannot fit curve using dates, so we need to convert it
        # to floats
        try:
            datesInMillisecond = []
            for i in range(0, len(dates)):
                datesInMillisecond.append( (dates[i] - dates[0]).days + 20 )
                # I have considered an initial offset, considering that
                # the data I've collected starts on the 6th of March,
                # but there already have been, by that date, numerous cases
            return datesInMillisecond
        except Exception as e:
            print(colored("The following exception was catched:" + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))
