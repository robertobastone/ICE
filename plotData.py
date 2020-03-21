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
        y2, x2 = self.gettingDailyIncrement(table,region,dates,idx)
        # PLOTTING
        fig, (ax_plt, ax_incr) = plt.subplots(  nrows=2,
                                                ncols=1,
                                                sharex=True,
                                                figsize=(12, 10)
                                              )
        # FIRST SUBPLOT
        ax_plt.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
        ax_plt.plot(dates,y, zorder=5)
        ax_plt.scatter(dates,y, zorder=10)
        ax_plt.set_ylabel("Cases (ICU + hospitalised + self-quarantined)")
        ax_plt.text(lockdownStartDate, table.iloc[idx][-1], lockdown)
        # SECOND SUBPLOT
        ax_incr.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 1e3, alpha=0.125, color='r', zorder=0)
        ax_incr.plot(x2,y2,zorder=5)
        ax_incr.scatter(x2,y2, zorder=10)
        ax_incr.set_ylabel("Daily Increment (%)")
        ax_incr.text(lockdownStartDate, y2[-1], lockdown)
        # SHARED PLOT SETTINGS
        ax_plt.set_title(region[idx])
        ax_incr.set_xlabel("Days")
        ax_incr.set_xticklabels(xlabels, rotation=40, ha="right")
        # SAVE PLOT
        filename = 'plots/'+region[idx]+'_covid19_cases.png'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename, bbox_inches='tight',dpi=400)

    def gettingDailyIncrement(self,table,region,dates,idx):
        dailyIncrementsList = []
        y = table.iloc[idx][1:]
        x = dates[1:]
        for i in range(1,len(y)):
            dailyIncrement = ((y[i]-y[i-1])/y[i-1])*100
            #dailyIncrement = y[i]-y[i-1]
            dailyIncrementsList.append(dailyIncrement)
        return dailyIncrementsList, x
