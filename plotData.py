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
        # DATA
        y = table.iloc[idx][1:]
        xlabels = [str(datetime.date(dates[i])) for i in range(0, len(dates))]
        y2, y3, x2 = self.gettingDailyIncrement(table,region,dates,idx)
        # PLOTTING
        fig, (ax_plt, ax_abs, ax_incr) = plt.subplots(  nrows=3,
                                                ncols=1,
                                                sharex=True,
                                                figsize=(12, 20)
                                              )
        # FIRST SUBPLOT
        ax_plt.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
        ax_plt.plot(dates,y, zorder=5)
        ax_plt.scatter(dates,y, zorder=10)
        ax_plt.set_ylabel("Cases (ICU + hospitalised + self-quarantined)")
        ax_plt.text(lockdownStartDate, table.iloc[idx][-1], lockdown)
        # SECOND SUBPLOT
        ax_abs.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 1e3, alpha=0.125, color='r', zorder=0)
        ax_abs.plot(x2,y2,zorder=5)
        ax_abs.scatter(x2,y2, zorder=10)
        ax_abs.set_ylabel("Daily Increment")
        # THIRD SUBPLOT
        ax_incr.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 1e3, alpha=0.125, color='r', zorder=0)
        ax_incr.plot(x2,y3,zorder=5)
        ax_incr.scatter(x2,y3, zorder=10)
        ax_incr.set_ylabel("Relative Daily Increment (%)")
        # SHARED PLOT SETTINGS
        ax_plt.set_title(region[idx])
        ax_incr.set_xlabel("Days")
        ax_incr.set_xticklabels(xlabels, rotation=40, ha="right")
        # SAVE PLOT
        filename = 'plots/'+region[idx]+'_covid19_cases.png'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.tight_layout()
        plt.savefig(filename, bbox_inches='tight',dpi=400)
        print(colored(region[idx] + " plotted ", 'blue'))

    def gettingDailyIncrement(self,table,region,dates,idx):
        dailyIncrementsList = []
        absoluteDailyIncrementsList = []
        y = table.iloc[idx][1:]
        x = dates[1:]
        for i in range(1,len(y)):
            dailyIncrement = ((y[i]-y[i-1])/y[i-1])*100
            dailyIncrementsList.append(dailyIncrement)
            absoluteDailyIncrement = y[i]-y[i-1]
            absoluteDailyIncrementsList.append(absoluteDailyIncrement)
        return absoluteDailyIncrementsList, dailyIncrementsList, x
