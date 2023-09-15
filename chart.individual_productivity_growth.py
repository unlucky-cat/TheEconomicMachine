# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy

iterations_count = 20
items_count = 4

economy = Economy(items_count)
economy.Iterate(iterations_count)

x_axis = np.arange(0, iterations_count, step=1)

for i in range(items_count):
    y_axis = economy._units[i]._history_data["productivity"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line1', linestyle='-', marker='o')

plt.xticks(x_axis)


# for i,j in zip(x_axis,y_axis):
#    plt.annotate(str(j), xy=(i,j))

plt.show()