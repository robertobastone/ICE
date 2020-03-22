################################################### PEER

author = 'Roberto Bastone'
email = 'robertobastone93@gmail.com'

version = 1.03

######################### LIBRARIES #########################
from termcolor import colored # customize ui
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
            table, region, dates = l.main()
            print(colored("Loading completed.", 'blue'))
            p = plotting.plotData()
            for i in range(0,len(region)):
                p.main(table, region, dates, i)
        except Exception as e:
            print(colored("Loading data failed", 'red'))
