# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy

iterations_count = 20
items_count = 10

economy = Economy(items_count)
economy.Iterate(iterations_count)

x_axis = np.arange(0, iterations_count, step=1)
plt.xticks(x_axis)

for i in range(items_count):
    y_axis = economy._units[i]._goods_produced_history
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line1', linestyle='solid', marker='o')

    y_axis = economy._units[i]._needs_growing_history
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line2', linestyle='dotted', marker='+')




    plt.show()

