######################### LIBRARIES #########################
import os # info about file
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

    def main(self):
        try:
            table = pd.read_excel(dataLocation) # open table
            tableColumns = table.columns.ravel()
            dates = tableColumns[1:] # create dates array
            region = table['Region'] # create region array
            return table, region, dates
        except Exception as e:
            print(colored("Make sure you have " + dataLocation + " in the same directory of the ICE bundle.", 'red'))
