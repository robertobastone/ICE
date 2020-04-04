######################### LIBRARIES #########################
from termcolor import colored # customize ui
import sys # better management of the exceptions
from scipy.optimize import curve_fit # fit logistic curve
import numpy as np
import csv
import string
alphabet = list(string.ascii_lowercase)  # the whole latin alphabet


class fitData:

    def __init__(self):
        print(colored("Fitting data... ", 'blue'))

    def sigmoid_1(self, x, a, b, c):
        y = a / (1 + b * np.exp(c*np.negative(x)))
        return y

    def sigmoid_2(self, x, a, b, c, e):
        y = a / (1 + b * np.exp(c * np.negative(x - e)))
        return y

    def plotLogistGrowthFit(self,xdata,ydata):
        try:
            popt, pcov = curve_fit(self.sigmoid_1, xdata, ydata)
            #popt2, pcov2 = curve_fit(self.sigmoid_2, xdata, ydata, bounds=([-np.inf,0,-np.inf, -np.inf],np.inf), maxfev=50000)
            #print(colored(popt2, 'blue'))
            # pcov is the estimated covariance matrix of popt
            # the diagonals provide the variance of the parameter estimate
            perr = np.sqrt(np.diag(pcov))
            with open('results.csv', 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                                 quotechar='|',
                                                 quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['Parameter', 'Estimate', '1sigma'])
                for i in range(0,len(popt)):
                    filewriter.writerow([alphabet[i], popt[i], perr[i]])
            print(colored("Fitting completed", 'blue'))
            return popt
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(colored("The following exception was catched: " + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))
