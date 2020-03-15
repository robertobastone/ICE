######################### LIBRARIES #########################
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

lockdown = 'italy national lockdown start date'

table = pd.read_excel('data.xlsx')

tableColumns = table.columns.ravel()

dates = tableColumns[1:]
region = table['Region']

#x = table.iloc[idxR][1:]

#print(dates)

######################### PLOTTING #########################
for i in range(0,len(region)):
    x = table.iloc[i][1:]
    plt.figure(figsize=(9, 6))
    #Italy coronavirus lockdown declared
    plt.axvline(x = dates[2],ymin = 0, ymax = 2e3, color='r')
    plt.plot(dates,x)
    plt.scatter(dates,x)
    plt.title(region[i])
    plt.ylabel("Cases (ICU + hospitalised + self-quarantined)")
    plt.xlabel("Days")
    plt.xticks(rotation=70, ha="right")
    # cambiare in legend
    plt.text(dates[2], table.iloc[i][2] * ( 1 + 0.75), lockdown, rotation = 90, color = 'r')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    #plt.show()
    filename = 'plots/'+region[i]+'_covid19_cases.png'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, bbox_inches='tight',dpi=400)
