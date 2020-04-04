######################### LIBRARIES #########################
import os # info about file
import sys # better management of the exceptions
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from termcolor import colored # customize ui
from datetime import datetime # managing datatime records
import fitData as fitting

lockdown = 'Italy national lockdown'
lockdownStartDate = datetime(2020,3,9)

class plotData:

    def __init__(self):
        print(colored("Plotting data... ", 'blue'))

    def plotActiveCases(self, table, region, dates, idx):
        try:
            # DATA
            y = table.iloc[idx][1:]
            y2, y3, x2 = self.gettingDailyIncrement(table,region,dates,idx)
            # PLOTTING
            fig, (ax_plt, ax_abs, ax_incr) = plt.subplots(  nrows=3,
                                                            ncols=1,
                                                            sharex=True,
                                                            figsize=(12, 20)
                                                         )
            # FIRST SUBPLOT: TOTAL CASES VS TIME
            ax_plt.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_plt.plot(dates, y, zorder=5)
            ax_plt.scatter(dates, y, zorder=10)
            ax_plt.set_ylabel("Cases (ICU + hospitalised + self-quarantined)")
            ax_plt.text(lockdownStartDate, table.iloc[idx][-1], lockdown)
            # SECOND SUBPLOT: DAILY INCREMENT VS TIME
            ax_abs.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 1e3, alpha=0.125, color='r', zorder=0)
            ax_abs.plot(x2,y2,zorder=5)
            ax_abs.scatter(x2,y2, zorder=10)
            ax_abs.set_ylabel("Daily Increment")
            # THIRD SUBPLOT: RELATIVE DAILY INCREMENT (%) VS TIME
            ax_incr.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 1e3, alpha=0.125, color='r', zorder=0)
            ax_incr.plot(x2,y3,zorder=5)
            ax_incr.scatter(x2,y3, zorder=10)
            ax_incr.set_ylabel("Relative Daily Increment (%)")
            # SHARED PLOT SETTINGS
            ax_plt.set_title(region[idx])
            ax_incr.set_xlabel("Days")
            ax_incr.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
            plt.setp(ax_incr.get_xticklabels(), rotation=40, horizontalalignment='right')
            # SAVE PLOT
            filename = 'activeCases/'+region[idx]+'_covid19_cases.png'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            plt.tight_layout()
            plt.savefig(filename, bbox_inches='tight',dpi=400)
            plt.close(fig)
            print(colored(region[idx] + " plotted ", 'blue'))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(colored("The following exception was catched: " + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))

    def plotTotalCases(self, table, groups, dates, datesInMillisecond, idx):
        try:
            # DATA
            y = table.iloc[idx][1:]
            y2, y3, x2 = self.gettingDailyIncrement(table,groups,dates,idx)
            # PLOTTING
            fig, (ax_plt) = plt.subplots(   nrows=1,
                                            ncols=1,
                                            sharex=True,
                                            figsize=(20, 12)
                                        )
            if (groups[idx] == 'Total number of cases'):
                f = fitting.fitData()
                popt = f.plotLogistGrowthFit(datesInMillisecond, y)
                ax_plt.plot(dates, f.sigmoid_1(datesInMillisecond, popt[0],
                                                                    popt[1],
                                                                    popt[2]), color='orange', label="Logistic Growth model", zorder=50)
                '''
                ax_plt.plot(dates, f.sigmoid_2(datesInMillisecond, popt2[0],
                                                                    popt2[1],
                                                                    popt2[2],
                                                                    popt2[3]), color='yellow', label="Logistic Growth model 2", zorder=40)
                '''
                ax_plt.legend(loc='lower right')
            ax_plt.axvspan(xmin = lockdownStartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_plt.plot(dates, y, zorder=5)
            ax_plt.scatter(dates, y, zorder=10)
            ax_plt.set_ylabel("Total")
            ax_plt.set_xlabel("Days")
            ax_plt.text(lockdownStartDate, table.iloc[idx][-1], lockdown)
            ax_plt.set_title(groups[idx])
            ax_plt.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
            plt.setp(ax_plt.get_xticklabels(), rotation=40, horizontalalignment='right')
            # SAVE PLOT
            filename = 'totalCases/'+groups[idx]+'_covid19_cases.png'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            plt.tight_layout()
            plt.savefig(filename, bbox_inches='tight',dpi=400)
            print(colored(groups[idx] + " plotted ", 'blue'))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(colored("The following exception was catched: " + str(e), 'red'))
            print(colored(str(exc_tb.tb_frame.f_code.co_filename) + " at  line " + str(exc_tb.tb_lineno), 'red'))

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
