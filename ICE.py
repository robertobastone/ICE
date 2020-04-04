################################################### PEER

author = 'Roberto Bastone'
email = 'robertobastone93@gmail.com'

version = 1.04

######################### LIBRARIES #########################
from termcolor import colored # customize ui
import sys # better management of the exceptions
import loadData as loading
import plotData as plotting

class ICE:
    def __init__(self):
        print(colored("Initializing... Italy Covid19 Epidemic version " + str(version), 'blue'))
        print(colored("(Author: " + author+')', 'blue'))
        print(colored("For info - or anything else - please, feel free to reach me at " + email, 'blue'))

    def main(self):
        try:
            l = loading.loadData()
            table_1, region, dates = l.activeCases()
            table_2, groups, dates, datesInMillisecond = l.totalCases()
            print(colored("Loading completed.", 'blue'))
            p = plotting.plotData()
            for i in range(0,len(region)):
                p.plotActiveCases(table_1, region, dates, i)
            for i in range(0,len(groups)):
                p.plotTotalCases(table_2, groups, dates, datesInMillisecond, i)
        except Exception as e:
            print(colored("The following exception was catched: " + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))
