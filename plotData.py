######################### LIBRARIES #########################
import os # info about file
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from termcolor import colored # customize ui
from datetime import datetime # managing datatime records

lockdown = 'Italy national lockdown'
lockdownStartDate = datetime(2020,3,9)

class plotData:

    def __init__(self):
        print(colored("Plotting data... ", 'blue'))

    def main(self, table, region, dates, idx):
        plt.figure(figsize=(9, 6))
        x = table.iloc[idx][1:]
        plt.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
        plt.plot(dates,x, zorder=5)
        plt.scatter(dates,x, zorder=10)
        plt.title(region[idx])
        plt.ylabel("Cases (ICU + hospitalised + self-quarantined)")
        plt.xlabel("Days")
        plt.xticks(rotation=40, ha="right")
        # cambiare in legend
        plt.text(lockdownStartDate, table.iloc[idx][1], lockdown)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        #plt.show()
        filename = 'plots/'+region[idx]+'_covid19_cases.png'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename, bbox_inches='tight',dpi=400)
