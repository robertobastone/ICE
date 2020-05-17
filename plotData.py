######################### LIBRARIES #########################
import os # info about file
import sys # better management of the exceptions
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from termcolor import colored # customize ui
from datetime import datetime # managing datatime records
import fitData as fitting

phase1 = 'Phase 1: national lockdown'
phase1StartDate = datetime(2020,3,9)
phase2 = 'Phase 2: partial re-opening'
phase2StartDate = datetime(2020,5,4)


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
            ax_plt.axvspan(xmin = phase1StartDate, xmax= phase2StartDate, ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_plt.axvspan(xmin = phase2StartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='orange', zorder=0)
            ax_plt.plot(dates, y, zorder=5)
            ax_plt.scatter(dates, y, zorder=10)
            ax_plt.set_ylabel("Cases (ICU + hospitalised + self-quarantined)", fontsize=15)
            ax_plt.text(phase1StartDate, table.iloc[idx][-5], phase1, fontsize=13)
            ax_plt.text(phase2StartDate, table.iloc[idx][-5], phase2, fontsize=13)
            ax_plt.set_ylim(bottom=0)
            # SECOND SUBPLOT: DAILY INCREMENT VS TIME
            ax_abs.axvspan(xmin = phase1StartDate, xmax= phase2StartDate, ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_abs.axvspan(xmin = phase2StartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='orange', zorder=0)
            ax_abs.plot(x2,y2,zorder=5)
            ax_abs.scatter(x2,y2, zorder=10)
            ax_abs.axhline(y=0, color = 'black')
            ax_abs.set_ylabel("Daily Increment", fontsize=15)
            # THIRD SUBPLOT: RELATIVE DAILY INCREMENT (%) VS TIME
            ax_incr.axvspan(xmin = phase1StartDate, xmax= phase2StartDate, ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_incr.axvspan(xmin = phase2StartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='orange', zorder=0)
            ax_incr.plot(x2,y3,zorder=5)
            ax_incr.scatter(x2,y3, zorder=10)
            ax_incr.axhline(y=0, color = 'black')
            ax_incr.set_ylabel("Relative Daily Increment (%)", fontsize=15)
            # SHARED PLOT SETTINGS
            ax_plt.set_title(region[idx], fontsize=20)
            ax_incr.set_xlabel("Days", fontsize=15)
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

    def plotTotalCases(self, table, groups, dates, datesInDays, idx):
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
                popt = f.plotLogistGrowthFit(datesInDays, y)
                ax_plt.plot(dates, f.sigmoid_1(datesInDays, popt[0],
                                                                    popt[1],
                                                                    popt[2]), color='orange', label="Logistic Growth model", zorder=50)
                '''
                ax_plt.plot(dates, f.sigmoid_2(datesInDays, popt2[0],
                                                                    popt2[1],
                                                                    popt2[2],
                                                                    popt2[3]), color='sienna', label="Logistic Growth model 2", zorder=40)
                '''
                ax_plt.legend(loc='lower right')
            ax_plt.axvspan(xmin = phase1StartDate, xmax= phase2StartDate, ymin = 0, ymax = 2e3, alpha=0.125, color='r', zorder=0)
            ax_plt.axvspan(xmin = phase2StartDate, xmax= dates[-1], ymin = 0, ymax = 2e3, alpha=0.125, color='orange', zorder=0)
            ax_plt.plot(dates, y, zorder=5)
            ax_plt.scatter(dates, y, zorder=10)
            ax_plt.set_ylabel("Total", fontsize=15)
            ax_plt.set_xlabel("Days", fontsize=15)
            ax_plt.set_ylim(bottom=0)
            ax_plt.text(phase1StartDate, table.iloc[idx][-5], phase1, fontsize=13)
            ax_plt.text(phase2StartDate, table.iloc[idx][-5], phase2, fontsize=13)
            ax_plt.set_title(groups[idx], fontsize=20)
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

    def plotEvolutionOfSigmoidParameter(self, ydata, xdata):
        try:
            #FITTING
            f = fitting.fitData()
            poptList, pcovList, numberOfDays = f.keepTrackOfSigmoidParameterEvolution(xdata, ydata)
            aParam = [x[0] for x in poptList]
            aParamError = [x[0] for x in pcovList]
            bParam = [x[1] for x in poptList]
            bParamError = [x[1] for x in pcovList]
            cParam = [x[2] for x in poptList]
            cParamError = [x[2] for x in pcovList]
            # PLOTTING
            fig, (ax_a, ax_b, ax_c) = plt.subplots(   nrows=3,
                                            ncols=1,
                                            sharex=True,
                                            figsize=(12, 20)
                                        )
            # FIRST SUBPLOT: PARAMETER A
            ax_a.plot(numberOfDays, aParam, zorder=5)
            ax_a.errorbar(numberOfDays, aParam, yerr=aParamError, fmt='o', color='dodgerblue', zorder=5)
            ax_a.set_ylabel(r'$a$', fontsize=15)
            # SECOND SUBPLOT: PARAMETER B
            ax_b.plot(numberOfDays, bParam, zorder=5)
            ax_b.errorbar(numberOfDays, bParam, yerr=bParamError, fmt='o', color='dodgerblue', zorder=5)
            ax_b.set_ylabel(r'$b$', fontsize=15)
            # THIRD SUBPLOT: PARAMETER C
            ax_c.plot(numberOfDays, cParam, zorder=5)
            ax_c.errorbar(numberOfDays, cParam, yerr=cParamError, fmt='o', color='dodgerblue', zorder=5)
            ax_c.set_ylabel(r'$c$', fontsize=15)
            # SHARED PLOT SETTINGS
            ax_a.set_title(r'Sigmoid 1 Parameters evolution', fontsize=20)
            ax_c.set_xlabel("Days", fontsize=15)
            filename = 'sigmoidsParameters/sigmoid_1_Params.png'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            plt.tight_layout()
            plt.savefig(filename, bbox_inches='tight',dpi=400)
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
