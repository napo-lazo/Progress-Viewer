import matplotlib.pyplot as plt
from Constants import *

def DisplayRecordsList(entryName: str, recordsList: list, asCumulative: bool) -> None:
    recordTotals = []
    dateLabels = []
    max = 0
    
    for record in recordsList:
        total = 0

        if (asCumulative):
            total = record[CUMULATIVE_TOTAL]
        else:
            for value in record[RECORDS_KEY]:
                total += value
        
        if (total > max):
            max = total

        recordTotals.append(total)
        dateLabels.append(record[START_DATE])

    xTicks = list(range(1, len(recordTotals)+1))

    _, ax = plt.subplots()
    
    ax.set_title(entryName)
    ax.set_xlabel("Dates")

    if (asCumulative):
        ax.plot(xTicks, recordTotals, 2, marker='o')
        counter = 0
        for record in recordTotals:
            ax.annotate(record, (xTicks[counter], record), textcoords='offset points', xytext=(-10, 10), ha='center')
            counter += 1
    else:
        rects = ax.bar(xTicks, recordTotals, 0.25)
        ax.bar_label(rects, padding=3)
    
    ax.set_xticks(xTicks)
    ax.set_xticklabels(dateLabels)
    ax.set_xlim(0,xTicks[-1] + 1)
    ax.set_ylim(0, max + max/5)

    plt.show()