# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy

iterations_count = 20
items_count = 1

economy = Economy(items_count)
economy.Iterate(iterations_count)

x_axis = np.arange(0, iterations_count, step=1)
plt.xticks(x_axis)

for i in range(items_count):
    y_axis = economy._units[i]._history_data["productivity"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line1', linestyle='solid', marker='o')

    y_axis = economy._units[i]._history_data["goods_produced"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line2', linestyle='dashed', marker='X')

    y_axis = economy._units[i]._history_data["needs_growing"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line3', linestyle='dotted', marker='+')

    y_axis = economy._units[i]._history_data["reminders"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line4', linestyle='dashdot', marker=',')

    tbl = pd.DataFrame.from_records(economy._units[i]._history_data)
    print(tbl)

    plt.show()
