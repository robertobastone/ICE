######################### LIBRARIES #########################
import os # info about file
from termcolor import colored # customize ui
import pandas as pd # open excel file
from datetime import datetime # managing datatime records

dataLocation ='data.xlsx'


class loadData:

    def __init__(self):
        mostRecentVersionDate = datetime.fromtimestamp(os.stat(dataLocation).st_mtime)
        print(colored("Loading data... " + str(mostRecentVersionDate), 'blue'))

    def main(self):
        table = pd.read_excel(dataLocation) # open table
        tableColumns = table.columns.ravel()
        dates = tableColumns[1:] # create dates array
        region = table['Region'] # create region array
        return table, region, dates
